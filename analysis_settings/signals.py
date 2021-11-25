from django.core.cache import cache
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from analysis_settings.models import Parameters, AnalyseReview

from analysis.tasks import process_nmea_report_file


@receiver(post_save, sender=Parameters)
def update_cache(sender, instance, *args, **kwargs):
    cache.set(instance.CACHE_KEY, Parameters.objects.last())


@receiver(m2m_changed, sender=AnalyseReview.reports.through)
def review_selected_reports(sender, instance, **kwargs):
    _ = [process_nmea_report_file.delay(id_) for id_ in instance.reports.values_list('id', flat=True)]
