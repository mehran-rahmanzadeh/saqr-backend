from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from analysis.models.report_model import Report
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

    def __str__(self):
        return f'Analysis Parameters {self.id}'

    class Meta:
        verbose_name = _('Parameters')
        verbose_name_plural = _('Parameters')


class AnalyseReview(TimeStampModelMixin):
    """Analyse Review Request Model"""
    reason = models.TextField(
        _('Review Reason'),
        null=True,
        blank=True,
        help_text=_('Nullable')
    )

    reports = models.ManyToManyField(
        Report,
        related_name='reviews',
        verbose_name=_('Reports')
    )

    submitted_by = models.ForeignKey(
        get_user_model(),
        related_name='reviews',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False
    )

    def __str__(self):
        return f'Analyse Review Request Submitted By {self.submitted_by}'

    class Meta:
        verbose_name = _('Analyse Review')
        verbose_name_plural = _('Analyse Reviews')
