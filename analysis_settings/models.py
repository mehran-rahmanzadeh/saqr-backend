from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from painless.utils.models.mixins import TimeStampModelMixin


class Parameters(TimeStampModelMixin):
    """Parameters Model"""
    CACHE_KEY = 'analysis_settings'

    speed_ratio = models.FloatField(
        _('Speed Ratio'),
        help_text=_('0 - 10'),
        default=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    accel_ratio = models.FloatField(
        _('Acceleration Ratio'),
        help_text=_('0 - 10'),
        default=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    alt_ratio = models.FloatField(
        _('Altitude Ratio'),
        help_text=_('0 - 10'),
        default=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    weight_ratio = models.FloatField(
        _('Weight Ratio'),
        help_text=_('0 - 10'),
        default=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    age_ratio = models.FloatField(
        _('Age Ratio'),
        help_text=_('0 - 10'),
        default=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        verbose_name = _('Parameters')
        verbose_name_plural = _('Parameters')
