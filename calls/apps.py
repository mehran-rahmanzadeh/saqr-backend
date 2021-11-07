"""
Auto Generated apps.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.apps import AppConfig


class CallsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calls'
    
    def ready(self):
        import calls.signals
    
