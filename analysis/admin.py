from django.contrib import admin

from analysis.models.report_model import Report, ReportDetail
from analysis.models.saqr_model import Saqr


class ReportDetailStackedAdminInline(admin.StackedInline):
    model = ReportDetail
    fk_name = 'report'
    readonly_fields = [
        'max_speed', 'avg_speed', 'max_accel',
        'avg_accel', 'max_alt', 'min_alt',
        'avg_alt', 'signal_status', 'avg_gps_count',
        'score'
    ]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    inlines = [
        ReportDetailStackedAdminInline
    ]
    list_display = ['sku', 'created', 'modified', 'created_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(ReportDetail)
class ReportDetailAdmin(admin.ModelAdmin):
    list_display = [
        'report', 'max_speed', 'avg_speed',
        'max_accel', 'avg_accel', 'max_alt',
        'min_alt', 'avg_alt', 'score'
    ]

    readonly_fields = [
        'max_speed', 'avg_speed', 'max_accel',
        'avg_accel', 'max_alt', 'min_alt',
        'avg_alt', 'signal_status', 'avg_gps_count',
        'score'
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Saqr)
class SaqrAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'age',
        'weight',
        'owner',
        'created',
        'modified'
    ]

    list_filter = [
        'created',
        'modified'
    ]

    search_fields = [
        'title',
    ]
