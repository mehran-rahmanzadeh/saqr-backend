"""
Auto Generated models.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

# validator support
from importlib import import_module
validators = import_module('django.core.validators')


# cache support
from cms.mixins import ModelCacheMixin


class ContactUs(models.Model, ModelCacheMixin):
    """
    ContactUs Model
    Auto generated
    """
    
    CACHE_KEY = 'contactus'  # auto generated CACHE_KEY
    
    title = models.CharField(
             max_length=255,
             
    )
    
    description = models.TextField(
             
    )
    
    tel = models.CharField(
             max_length=13,
             
    )
    
    email = models.CharField(
             max_length=255,
             
             validators=[
                
                getattr(validators, 'EmailValidator')(None),
                
             ]
             
    )
    
    created = models.DateTimeField(
             auto_now_add=True,
             
    )
    
    modified = models.DateTimeField(
             auto_now=True,
             
    )
    
    def __str__(self):
        return f"ContactUs {self.pk}" 

    class Meta:
        verbose_name = _("Contact us")  # auto generated verbose_name
        verbose_name_plural = _("Contact Us")
