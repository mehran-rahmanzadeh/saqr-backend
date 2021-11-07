from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from analysis.models import Report, ReportDetail

class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="50%" height="50%" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

class ReportDetailStackedAdminInline(admin.StackedInline):
    model = ReportDetail
    fk_name = 'report'
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
    readonly_fields = ['max_speed', 'avg_speed', 'max_accel', 'avg_accel', 'max_alt', 'min_alt', 'avg_alt', 'signal_status', 'avg_gps_count']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    inlines = [
        ReportDetailStackedAdminInline
    ]
    def image_tag(self, obj):
        return format_html('<img src="{}" width="60%" height="60%" />'.format(obj.report_detail.charts_image.url))

    image_tag.short_description = 'Image'
    list_display = ['image_tag', 'created', 'modified']

@admin.register(ReportDetail)
class ReportDetailAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="80%" height="80%" />'.format(obj.charts_image.url))

    image_tag.short_description = 'Image'
    list_display = ['image_tag', 'max_speed', 'avg_speed', 'max_accel', 'avg_accel', 'max_alt', 'min_alt', 'avg_alt']

    def has_add_permission(self, request):
        return False