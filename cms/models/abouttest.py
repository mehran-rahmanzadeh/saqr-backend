"""
Auto Generated models.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

# cache support
from cms.mixins import ModelCacheMixin


class AboutTest(models.Model, ModelCacheMixin):
    """
    AboutTest Model
    Auto generated
    """

    CACHE_KEY = 'abouttest'  # auto generated CACHE_KEY

    title = models.CharField(
        max_length=255,

    )

    description = models.TextField(

    )

    created = models.DateTimeField(
        auto_now_add=True,

    )

    modified = models.DateTimeField(
        auto_now=True,

    )

    def __str__(self):
        return f"AboutTest {self.pk}"

    class Meta:
        verbose_name = _("About test")  # auto generated verbose_name
        verbose_name_plural = _("About Tests")
