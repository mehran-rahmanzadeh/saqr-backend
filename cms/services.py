"""
Auto Generated services.py
Automatically generated with ❤️ by django-sage-painless
"""

from django.core.cache import cache


def clear_cache_for_model(cache_key: str):
    """
    removes all caches of this model
    """
    keys = cache.keys(f'*{cache_key}*')
    cache.delete_many(keys)
