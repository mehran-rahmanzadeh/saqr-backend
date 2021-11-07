"""
Auto Generated models.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


# cache support
from cms.mixins import ModelCacheMixin


class AboutDashboard(models.Model, ModelCacheMixin):
    """
    AboutDashboard Model
    Auto generated
    """
    
    CACHE_KEY = 'aboutdashboard'  # auto generated CACHE_KEY
    
    title = models.CharField(
             max_length=255,
             
    )
    
    description = models.TextField(
             
    )
    
    first_image = models.ImageField(
             
    )
    
    second_image = models.ImageField(
             
    )
    
    created = models.DateTimeField(
             auto_now_add=True,
             
    )
    
    modified = models.DateTimeField(
             auto_now=True,
             
    )
    
    def __str__(self):
        return f"AboutDashboard {self.pk}" 

    class Meta:
        verbose_name = _("About dashboard")  # auto generated verbose_name
        verbose_name_plural = _("About Dashboards")
