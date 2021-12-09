import datetime

import numpy as np
import pandas as pd

from django.conf import settings

from analysis_settings.services import ParametersHandler

debug = settings.DEBUG


class Parser:
    """Process GPS data"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.lon_array: np.ndarray
        self.alt_array: np.ndarray
        self.lat_array: np.ndarray
        self.speed_array: np.ndarray
        self.timestamp_array: np.ndarray
        self.datetime_array: np.ndarray
        self.accel_array = list()
        self.angle_array: np.ndarray

    @classmethod
    def read_file(cls, path: str):
        """
        :param: path: file path
        :return: pandas dataframe
        """
        file = pd.read_csv(path, sep=';')
        return file

    @property
    def max_speed(self):
        """:return: max value of speed array"""
        return self.speed_array.max() if self.speed_array.any() else 0

    @property
    def avg_speed(self):
        """:return: average of speed array"""
        return self.speed_array.mean() if self.speed_array.any() else 0

    @property
    def max_accel(self):
        """:return: maximum value of accel"""
        return self.accel_array.max() if self.accel_array.any() else 0

    @property
    def avg_accel(self):
        """:return: average of accel array"""
        return self.accel_array.mean() if self.accel_array.any() else 0

    @property
    def max_alt(self):
        """:return: maximum value of altitude"""
        return self.alt_array.max() if self.alt_array.any() else 0

    @property
    def avg_alt(self):
        """:return: average value of altitude"""
        return self.alt_array.mean() if self.alt_array.any() else 0

    @property
    def min_alt(self):
        """:return: minimum value of altitude"""
        return self.alt_array.min() if self.alt_array.any() else 0

    @property
    def normalized_alt(self):
        """:return: max alt that falcon took off"""
        return self.max_alt - self.min_alt if self.alt_array.any() else 0

    def calculate_flight_score(self):
        """calculate report score
        :return: calculated score based on speed, accel and alt
        """
        parameters = ParametersHandler.get_from_cache()
        speed_score = self.avg_speed * parameters.speed_ratio
        accel_score = self.avg_accel * parameters.accel_ratio
        alt_score = self.normalized_alt * parameters.alt_ratio
        return sum([speed_score, accel_score, alt_score])

    @classmethod
    def convert_string_to_timestamp(cls, string):
        """
        :param: string: datetime string
        :return: converted to timestamp
        """
        string = string.rstrip()
        element = datetime.datetime.strptime(string, '%m/%d/%Y %H:%M:%S')
        return datetime.datetime.timestamp(element)

    def create_timestamp_array(self, datetime_array):
        """
        :param: datetime_array: string datetime array
        :return: converted to timestamp array
        """
        return np.array(list(map(self.convert_string_to_timestamp, datetime_array)))

    def process(self):
        """main process method"""
        df = self.read_file(self.file_path)

        if debug:
            print('[INFO]: log file opened')

        self.lat_array = df['lat'].to_numpy()
        self.lon_array = df['lon'].to_numpy()
        self.alt_array = df['alt'].to_numpy()
        self.speed_array = df['speed'].to_numpy()
        self.angle_array = df['angle'].to_numpy()
        self.datetime_array = df['datetime'].to_numpy()

        if debug:
            print('[INFO]: first stage data fetched')

        self.timestamp_array = self.create_timestamp_array(self.datetime_array)

        if debug:
            print('[INFO]: timestamp array calculated')

        self.__calculate_accel(self.timestamp_array, self.speed_array)  # calculate accelerations with speed array

        if debug:
            print('[INFO]: accel array calculated')

    def __calculate_accel(self, time_array, speed_array):
        """calculate moment acceleration based in speed-time graph
        :param: time_array: timestamp array
        :param: speed_array: speed array
        """
        for index, (speed, time) in enumerate(zip(speed_array, time_array)):
            try:
                current_speed = speed / 3.6  # m/s
                next_speed = speed_array[index + 1] / 3.6
                current_time = time  # s
                next_time = time_array[index + 1]
                if not next_time == current_time:
                    accel = (next_speed - current_speed) / (next_time - current_time)  # m/s**2
                    self.accel_array.append(accel)
            except:
                pass

        self.accel_array = np.array(self.accel_array)  # convert to numpy array
