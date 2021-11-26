import secrets

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from analysis.models.saqr_model import Saqr
from painless.utils.models.mixins import Sku_Mixin, TimeStampModelMixin


class Report(Sku_Mixin, TimeStampModelMixin):
    """nmea report model"""
    nmea_file = models.FileField(_('NMEA File'))

    saqr = models.ForeignKey(
        Saqr,
        related_name='reports',
        on_delete=models.CASCADE
    )

    submitted_by = models.ForeignKey(
        get_user_model(),
        related_name='reports',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        editable=False
    )

    show_in_public_page = models.BooleanField(
        _('Is it allowed to show in public page'),
        default=True
    )

    def __str__(self):
        return f'Report for file {self.saqr}'

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'report-{secrets.token_urlsafe(8)}'
        super(Report, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')


class ReportDetail(TimeStampModelMixin):
    """NMEA file report processed detail"""
    report = models.OneToOneField(
        Report,
        on_delete=models.CASCADE,
        verbose_name=_('Report'),
        related_name='report_detail'
    )

    max_speed = models.FloatField(
        _('Max Speed (m/s)'),
        null=True,
        blank=True
    )

    avg_speed = models.FloatField(
        _('Average Speed (m/s)'),
        null=True,
        blank=True
    )

    max_accel = models.FloatField(
        _('Max Acceleration (m/s**2)'),
        null=True,
        blank=True
    )

    avg_accel = models.FloatField(
        _('Average Acceleration (m/s**2)'),
        null=True,
        blank=True
    )

    max_alt = models.FloatField(
        _('Max Altitude (m)'),
        null=True,
        blank=True
    )

    avg_alt = models.FloatField(
        _('Average Altitude (m)'),
        null=True,
        blank=True
    )

    min_alt = models.FloatField(
        _('Min Altitude (m)'),
        null=True,
        blank=True
    )

    signal_status = models.CharField(
        _('Signal Status'),
        max_length=5,
        null=True,
        blank=True
    )

    avg_gps_count = models.IntegerField(
        _('Average GPS Count'),
        null=True,
        blank=True
    )

    score = models.PositiveIntegerField(
        _('Score'),
        default=0
    )

    lon_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Longitude Array'),
        editable=False,
        null=True,
        blank=True
    )
    alt_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Altitude Array'),
        editable=False,
        null=True,
        blank=True
    )
    sep_array = ArrayField(
        models.CharField(max_length=255),
        verbose_name=_('Sep Array'),
        editable=False,
        null=True,
        blank=True
    )
    lat_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Latitude Array'),
        editable=False,
        null=True,
        blank=True
    )
    track_array = ArrayField(
        models.CharField(max_length=255),
        verbose_name=_('Track Array'),
        editable=False,
        null=True,
        blank=True
    )
    speed_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Speed Array'),
        editable=False,
        null=True,
        blank=True
    )
    timestamp_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Timestamp Array'),
        editable=False,
        null=True,
        blank=True
    )
    accel_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Acceleration Array'),
        editable=False,
        null=True,
        blank=True
    )
    utc_array = ArrayField(
        models.FloatField(),
        verbose_name=_('UTC Array'),
        editable=False,
        null=True,
        blank=True
    )
    sip_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Sip Array'),
        editable=False,
        null=True,
        blank=True
    )
    fix_array = ArrayField(
        models.FloatField(),
        verbose_name=_('Fix Array'),
        editable=False,
        null=True,
        blank=True
    )
    sv_array = ArrayField(
        models.FloatField(),
        verbose_name=_('SV Array'),
        editable=False,
        null=True,
        blank=True
    )
    status_array = ArrayField(
        models.CharField(max_length=255),
        verbose_name=_('Status Array'),
        editable=False,
        null=True,
        blank=True
    )
    quality_array = ArrayField(
        models.CharField(max_length=255),
        verbose_name=_('Quality Array'),
        editable=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Report Detail for {self.report.saqr}'

    class Meta:
        verbose_name = _('Report Detail')
        verbose_name_plural = _('Report Details')
        ordering = ('-score',)
