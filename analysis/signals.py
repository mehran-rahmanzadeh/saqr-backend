from django.db.models.signals import post_save
from django.dispatch import receiver

from analysis.models.report_model import Report
from analysis.tasks import process_nmea_report_file


@receiver(post_save, sender=Report)
def process_ubx_file(sender, instance, *args, **kwargs):
    process_nmea_report_file.apply_async(countdown=3, kwargs={'report_instance': instance.id})
