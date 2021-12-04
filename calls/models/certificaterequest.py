"""
Auto Generated models.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

# validator support
from importlib import import_module

from painless.utils.regex.patterns import INTERNATIONAL_PHONE_NUMBER_PATTERN

validators = import_module('django.core.validators')


# cache support
from calls.mixins import ModelCacheMixin


class CertificateRequest(models.Model, ModelCacheMixin):
    """
    CertificateRequest Model
    Auto generated
    """
    
    CACHE_KEY = 'certificaterequest'  # auto generated CACHE_KEY
    
    phone_number = models.CharField(
             max_length=13,
             validators=[
                getattr(validators, 'RegexValidator')(INTERNATIONAL_PHONE_NUMBER_PATTERN),
             ]
    )

    date = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField(null=True, blank=True)
    
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
        return f"CertificateRequest {self.pk}" 

    class Meta:
        verbose_name = _("Certificate Request")  # auto generated verbose_name
        verbose_name_plural = _("Certificate Requests")
