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
from calls.mixins import ModelCacheMixin


class GetInTouch(models.Model, ModelCacheMixin):
    """
    GetInTouch Model
    Auto generated
    """
    
    CACHE_KEY = 'getintouch'  # auto generated CACHE_KEY
    
    name = models.CharField(
             max_length=50,
             
    )
    
    email = models.CharField(
             max_length=100,
             
             validators=[
                
                getattr(validators, 'EmailValidator')(None),
                
             ]
             
    )
    
    subject = models.CharField(
             max_length=100,
             
    )
    
    phone = models.CharField(
             max_length=13,
             null=True,
             blank=True,
             
    )
    
    message = models.TextField(
             
    )
    
    seen = models.BooleanField(
             default=False,
             
    )
    
    created = models.DateTimeField(
             auto_now_add=True,
             
    )
    
    modified = models.DateTimeField(
             auto_now=True,
             
    )
    
    def __str__(self):
        return f"GetInTouch {self.pk}" 

    class Meta:
        verbose_name = _("Get in touch")  # auto generated verbose_name
        verbose_name_plural = _("Get In Touches")
