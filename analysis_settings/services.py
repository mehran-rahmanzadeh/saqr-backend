from django.core.cache import cache

from analysis_settings.models import Parameters


class ParametersHandler:
    """Analysis Parameters Handler"""
    analysis_cache_key = 'analysis_settings'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def set_to_cache(cls):
        """set param to cache"""
        cache.set(cls.analysis_cache_key, Parameters.objects.last())

    @classmethod
    def get_from_cache(cls):
        """get param from cache"""
        return cache.get_or_set(cls.analysis_cache_key, Parameters.objects.last())
