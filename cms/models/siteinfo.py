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


class SiteInfo(models.Model, ModelCacheMixin):
    """
    SiteInfo Model
    Auto generated
    """

    CACHE_KEY = 'siteinfo'  # auto generated CACHE_KEY

    title = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    logo = models.ImageField(

        validators=[

            getattr(
                validators,
                'FileExtensionValidator')(
                allowed_extensions=[
                    'svg',
                    'SVG',
                    'webp',
                    'png',
                    'PNG']),

        ]

    )

    tel = models.CharField(
        max_length=255,

    )

    email = models.CharField(
        max_length=255,

        validators=[

            getattr(validators, 'EmailValidator')(None),

        ]

    )

    address = models.CharField(
        max_length=255,

    )

    instagram = models.CharField(
        max_length=255,

    )

    facebook = models.CharField(
        max_length=255,

    )

    twitter = models.CharField(
        max_length=255,

    )

    linkedin = models.CharField(
        max_length=255,

    )

    whatsapp = models.CharField(
        max_length=255,

    )

    footer = models.CharField(
        max_length=255,

    )

    created = models.DateTimeField(
        auto_now_add=True,

    )

    modified = models.DateTimeField(
        auto_now=True,

    )

    def __str__(self):
        return f"SiteInfo {self.pk}"

    @property
    def get_instagram_url(self):
        return f'https://www.instagram.com/{self.instagram}/'

    @property
    def get_whatsapp_url(self):
        return f'https://wa.me/message/{self.whatsapp}/'

    @property
    def get_twitter_url(self):
        return f'https://www.twitter.com/{self.twitter}/'

    @property
    def get_facebook_url(self):
        return f'https://www.facebook.com/{self.facebook}/'

    class Meta:
        verbose_name = _("Site info")  # auto generated verbose_name
        verbose_name_plural = _("Site Info")
