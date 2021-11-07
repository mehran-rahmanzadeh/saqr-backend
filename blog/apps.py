"""
Auto Generated apps.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
    def ready(self):
        import blog.signals
    
