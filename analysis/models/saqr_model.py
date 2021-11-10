import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from painless.utils.models.mixins import (
    Sku_Mixin,
    TimeStampModelMixin,
    TitleSlugLinkModelMixin
)


class Saqr(Sku_Mixin, TimeStampModelMixin, TitleSlugLinkModelMixin):
    """SAQR model"""
    weight = models.PositiveIntegerField(
        _('Weight'),
        null=True,
        blank=True
    )

    age = models.PositiveIntegerField(
        _('Age'),
        null=True,
        blank=True
    )

    owner = models.ForeignKey(
        get_user_model(),
        related_name='saqrs',
        on_delete=models.CASCADE
    )

    is_verified = models.BooleanField(
        _('Is Verified'),
        default=False
    )

    def __str__(self):
        return f'SAQR {self.title} owned by {self.owner}'

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'saqr-{secrets.token_urlsafe(8)}'
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Saqr, self).save(*args, **kwargs)
