from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from analysis_settings.models import Parameters


@receiver(post_save, sender=Parameters)
def update_cache(sender, instance, *args, **kwargs):
    cache.set(instance.CACHE_KEY, Parameters.objects.last())
