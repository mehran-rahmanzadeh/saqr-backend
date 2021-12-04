import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from analysis_settings.services import ParametersHandler
from painless.utils.models.mixins import (
    Sku_Mixin,
    TimeStampModelMixin
)


class SaqrImage(Sku_Mixin, TimeStampModelMixin):
    """SAQR Image model"""
    image = models.ImageField(
        _('Image'),
        upload_to='saqr-images/'
    )

    def __str__(self):
        return self.image.url
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'img-{secrets.token_urlsafe(8)}'
        super(SaqrImage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Saqr Image')
        verbose_name_plural = _('Saqr Images')


class Saqr(Sku_Mixin, TimeStampModelMixin):
    """SAQR model"""
    name = models.CharField(
        _('Name'),
        max_length=255,
        null=True,
        blank=True
    )

    birth_date = models.DateField(
        _('Birth Date'),
        null=True,
        blank=True
    )

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

    images = models.ManyToManyField(
        SaqrImage,
        blank=True,
        related_name='saqrs'
    )

    passport_image = models.ImageField(
        _('Passport Image'),
        null=True,
        blank=True,
        upload_to='saqr-passports/'
    )

    profile_image = models.ImageField(
        _('Profile Image'),
        upload_to='saqr-profile-images/',
        null=True,
        blank=True
    )

    cover = models.ImageField(
        _('Cover Image'),
        upload_to='saqr-profile-covers/',
        null=True,
        blank=True
    )

    owner = models.OneToOneField(
        get_user_model(),
        related_name='saqr',
        on_delete=models.CASCADE
    )

    is_verified = models.BooleanField(
        _('Is Verified'),
        default=False
    )

    submitted_by = models.ForeignKey(
        get_user_model(),
        related_name='submitted_saqrs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False
    )

    def __str__(self):
        return f'SAQR {self.name} owned by {self.owner}'

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'saqr-{secrets.token_urlsafe(8)}'
        super(Saqr, self).save(*args, **kwargs)

    def calculate_fundamental_score(self):
        """calculate score based on age, weight and ..."""
        parameters = ParametersHandler.get_from_cache()
        weight_score = self.weight * parameters.weight_ratio if self.weight else 0
        age_score = self.age * parameters.age_ratio if self.age else 0
        return sum([weight_score, age_score])
