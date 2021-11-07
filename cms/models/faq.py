"""
Auto Generated models.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


# cache support
from cms.mixins import ModelCacheMixin


class Faq(models.Model, ModelCacheMixin):
    """
    Faq Model
    Auto generated
    """
    
    CACHE_KEY = 'faq'  # auto generated CACHE_KEY
    
    question = models.CharField(
             max_length=255,
             
    )
    
    answer = models.TextField(
             
    )
    
    created = models.DateTimeField(
             auto_now_add=True,
             
    )
    
    modified = models.DateTimeField(
             auto_now=True,
             
    )
    
    def __str__(self):
        return f"Faq {self.pk}" 

    class Meta:
        verbose_name = _("Faq")  # auto generated verbose_name
        verbose_name_plural = _("Faqs")
