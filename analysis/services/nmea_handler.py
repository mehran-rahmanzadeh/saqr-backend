import datetime

from statistics import mean

import numpy as np
from django.conf import settings

from pynmeagps import NMEAReader, NMEAParseError
from pynmeagps.nmeamessage import NMEAMessage
from pykalman import KalmanFilter

from analysis_settings.services import ParametersHandler

debug = settings.DEBUG


class Parser:
    """Parse NMEA raw data"""

    def __init__(self, ubx_file_path: str):
        self.file_path = ubx_file_path
        self.lon_array = list()
        self.alt_array = list()
        self.sep_array = list()
        self.lat_array = list()
        self.track_array = list()
        self.speed_array = list()
        self.timestamp_array = list()
        self.accel_array = list()
        self.utc_array = list()
        self.sip_array = list()
        self.fix_array = list()
        self.sv_array = list()
        self.status_array = list()
        self.quality_array = list()

    @classmethod
    def read_file(cls, path: str):
        """read ubx file"""
        return open(path, 'rb').readlines()

    @property
    def max_speed(self):
        return max(self.speed_array) if self.speed_array else 0

    @property
    def avg_speed(self):
        return mean(self.speed_array) if self.speed_array else 0

    @property
    def max_accel(self):
        return max(self.accel_array) if self.accel_array else 0

    @property
    def avg_accel(self):
        return mean(self.accel_array) if self.accel_array else 0

    @property
    def max_alt(self):
        return max(self.alt_array) if self.alt_array else 0

    @property
    def avg_alt(self):
        return mean(self.alt_array) if self.alt_array else 0

    @property
    def min_alt(self):
        return min(self.alt_array) if self.alt_array else 0

    @property
    def normalized_alt(self):
        return self.max_alt - self.min_alt if self.max_alt and self.min_alt else 0

    @property
    def signal_status(self):
        return max(set(self.status_array), key=self.status_array.count) if self.status_array else ''

    @property
    def avg_gps_count(self):
        return round(mean(self.sv_array), 1) if self.sv_array else 0

    @classmethod
    def __apply_kalman_filter(cls, x_data, y_data):
        """apply kalman filter on gps data"""
        if not x_data or not y_data:
            return x_data, y_data
        measure_data = [[x, y] for x, y in zip(x_data, y_data)]
        measurements = np.asarray(measure_data)
        initial_state_mean = [
            measurements[0, 0],
            0,
            measurements[0, 1],
            0
        ]

        transition_matrix = [
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]

        observation_matrix = [
            [1, 0, 0, 0],
            [0, 0, 1, 0]
        ]

        kf = KalmanFilter(
            transition_matrices=transition_matrix,
            observation_matrices=observation_matrix,
            initial_state_mean=initial_state_mean
        )

        kf = kf.em(measurements, n_iter=100)
        (smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)

        return smoothed_state_means[:, 0], smoothed_state_means[:, 2]

    def calculate_flight_score(self):
        """calculate report score"""
        parameters = ParametersHandler.get_from_cache()
        speed_score = self.avg_speed * parameters.speed_ratio
        accel_score = self.avg_accel * parameters.accel_ratio
        alt_score = self.normalized_alt * parameters.alt_ratio
        return sum([speed_score, accel_score, alt_score])

    def process_nmea(self):
        """main process method"""
        data = self.read_file(self.file_path)

        if debug:
            print('[INFO]: nmea file opened')

        if not data:
            return None

        for gps_row in data:
            if not gps_row:
                continue

            try:
                parsed_data = NMEAReader.parse(bytes(gps_row))
            except NMEAParseError as e:
                if debug:
                    print(f'[ERROR]: {e}')
                parsed_data = None

            if parsed_data:

                if parsed_data.msgID == 'GSV':
                    self.__process_GSV(parsed_data)

                elif parsed_data.msgID == 'GLL':
                    self.__process_GLL(parsed_data)

                elif parsed_data.msgID == 'RMC':
                    self.__process_RMC(parsed_data)

                elif parsed_data.msgID == 'VTG':
                    self.__process_VTG(parsed_data)

                elif parsed_data.msgID == 'GGA':
                    self.__process_GGA(parsed_data)

                elif parsed_data.msgID == 'GSA':
                    self.__process_GSA(parsed_data)

                else:
                    print(f'message {parsed_data.msgID} not implemented')

        if debug:
            print('[INFO]: gps data fetched')

        self.__calculate_accel(self.timestamp_array, self.speed_array)  # calculate accelerations with speed array
        self.__normalize_data()

        if debug:
            print('[INFO]: accel array calculated')

    def __normalize_data(self):
        """remove empty values and reshape arrays"""
        min_len = min([len(self.lat_array), len(self.lon_array)])
        self.lat_array = self.lat_array[:min_len]
        self.lon_array = self.lon_array[:min_len]

        min_len = min([len(self.timestamp_array), len(self.alt_array), len(self.speed_array), len(self.accel_array)])
        self.timestamp_array = self.timestamp_array[:min_len]
        self.alt_array = self.alt_array[:min_len]
        self.speed_array = self.speed_array[:min_len]
        self.accel_array = self.accel_array[:min_len]

    def __process_GSV(self, msg: NMEAMessage):
        if msg.numSV != '':
            self.sv_array.append(msg.numSV)

    def __process_GLL(self, msg: NMEAMessage):
        if msg.lat and msg.lon:
            self.lat_array.append(msg.lat)
            self.lon_array.append(msg.lon)
        self.status_array.append(msg.status)

    def __process_RMC(self, msg: NMEAMessage):
        if msg.lat and msg.lon:
            self.lat_array.append(msg.lat)
            self.lon_array.append(msg.lon)
        if msg.spd:
            self.speed_array.append(msg.spd)
        if msg.date and msg.time:
            self.timestamp_array.append(
                datetime.datetime.combine(msg.date, msg.time).timestamp())
        self.status_array.append(msg.status)

    def __process_VTG(self, msg: NMEAMessage):
        pass

    def __process_GGA(self, msg: NMEAMessage):
        if msg.lat and msg.lon:
            self.lat_array.append(msg.lat)
            self.lon_array.append(msg.lon)
        if msg.numSV != '':
            self.sv_array.append(msg.numSV)
        if msg.alt:
            self.alt_array.append(msg.alt)
        self.sep_array.append(msg.sep)
        self.quality_array.append(msg.quality)

    def __process_GSA(self, msg: NMEAMessage):
        pass

    def __calculate_accel(self, time_array: list, speed_array: list):
        """calculate moment acceleration based in speed-time graph"""
        for index, (speed, time) in enumerate(zip(speed_array, time_array)):
            try:
                current_speed = speed  # m/s
                next_speed = speed_array[index + 1]
                current_time = time  # s
                next_time = time_array[index + 1]

                accel = (next_speed - current_speed) / (next_time - current_time)  # m/s**2
                self.accel_array.append(accel)
            except:
                pass
