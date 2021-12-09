from celery import shared_task

from analysis.models.report_model import Report, ReportDetail
from analysis.services.gps_handler import Parser


@shared_task
def process_nmea_report_file(*args, **kwargs):
    """process on NMEA report file and store in DB"""
    report_instance = kwargs.get('report_instance')
    print(f'report id : {report_instance}')
    instance = Report.objects.get(id=report_instance)
    saqr = instance.saqr

    parser = Parser(instance.nmea_file.path)
    parser.process()  # do process

    # submit result in db
    report_detail = ReportDetail.objects.get_or_create(report=instance)[0]

    # fetch process result
    report_detail.max_speed = parser.max_speed
    report_detail.avg_speed = parser.avg_speed
    report_detail.max_accel = parser.max_accel
    report_detail.avg_accel = parser.avg_accel
    report_detail.max_alt = parser.max_alt
    report_detail.avg_alt = parser.avg_alt
    report_detail.min_alt = parser.min_alt
    report_detail.normalized_alt = parser.normalized_alt

    # fetch array data
    report_detail.lon_array = list(parser.lon_array)
    report_detail.alt_array = list(parser.alt_array)
    report_detail.lat_array = list(parser.lat_array)
    report_detail.speed_array = list(parser.speed_array)
    report_detail.timestamp_array = list(parser.timestamp_array)
    report_detail.accel_array = list(parser.accel_array)
    report_detail.datetime_array = list(parser.datetime_array)

    # set score
    report_detail.score = parser.calculate_flight_score() + saqr.calculate_fundamental_score()

    report_detail.save()
