from django.apps import apps
from django.core.cache import cache


class ParametersHandler:
    """Analysis Parameters Handler"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def set_to_cache(cls):
        """set param to cache"""
        Parameters = apps.get_model('analysis_settings', 'Parameters')
        cache.set(Parameters.CACHE_KEY, Parameters.objects.last())

    @classmethod
    def get_from_cache(cls):
        """get param from cache"""
        Parameters = apps.get_model('analysis_settings', 'Parameters')
        return cache.get_or_set(Parameters.CACHE_KEY, Parameters.objects.last())
