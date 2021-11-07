import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import SimpleUploadedFile

from analysis.services.ubx_handler import Parser

class Report(models.Model):
    """nmea report model"""
    nmea_file = models.FileField(_('NMEA File'))

    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Report for file {self.nmea_file}'
    
    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')

class ReportDetail(models.Model):
    """nmea file report processed detail"""
    report = models.OneToOneField(
        Report,
        on_delete=models.CASCADE,
        verbose_name=_('Report'),
        related_name='report_detail'
    )

    max_speed = models.FloatField(_('Max Speed (m/s)'), null=True, blank=True)
    avg_speed = models.FloatField(_('Average Speed (m/s)'), null=True, blank=True)
    max_accel = models.FloatField(_('Max Accelration (m/s**2)'), null=True, blank=True)
    avg_accel = models.FloatField(_('Average Accelration (m/s**2)'), null=True, blank=True)
    max_alt = models.FloatField(_('Max Altitude (m)'), null=True, blank=True)
    avg_alt = models.FloatField(_('Average Altitude (m)'), null=True, blank=True)
    min_alt = models.FloatField(_('Min Altitude (m)'), null=True, blank=True)
    signal_status = models.CharField(_('Signal Status'), max_length=5, null=True, blank=True)
    avg_gps_count = models.IntegerField(_('Average GPS Count'), null=True, blank=True)

    charts_image = models.ImageField(_('Charts'), null=True, blank=True)

    
    def charts_image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape(self.charts_image.url)
        
    charts_image_tag.short_description = 'Charts'
    charts_image_tag.allow_tags = True

    def __str__(self):
        return f'Report Detail for {self.report.nmea_file}'
    
    class Meta:
        verbose_name = _('Report Detail')
        verbose_name_plural = _('Report Details')

@receiver(post_save, sender=Report)
def process_ubx_file(sender, instance, *args, **kwargs):

    # process GPS data
    parser = Parser(instance.nmea_file.path)
    parser.process_nmea()
    
    # submit result in db
    report_detail = ReportDetail.objects.get_or_create(
        report=instance
    )[0]
    report_detail.max_speed = parser.max_speed
    report_detail.avg_speed = parser.avg_speed
    report_detail.max_accel = parser.max_accel
    report_detail.avg_accel = parser.avg_accel
    report_detail.max_alt = parser.max_alt
    report_detail.avg_alt = parser.avg_alt
    report_detail.min_alt = parser.min_alt
    report_detail.signal_status = parser.signal_status
    report_detail.avg_gps_count = parser.avg_gps_count

    # chart
    file_path = parser.show_data_charts(save=True)
    report_detail.charts_image = SimpleUploadedFile(
            name=file_path.split('/')[-1],
            content=open(
                file_path,
                'rb').read(),
            content_type='image/png'
        )
    os.remove(file_path)
    report_detail.save()