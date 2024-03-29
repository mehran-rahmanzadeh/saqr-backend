from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from analysis.models.report_model import Report, ReportDetail
from analysis.models.saqr_model import Saqr, SaqrImage


class ReportDetailStackedAdminInline(admin.StackedInline):
    model = ReportDetail
    fk_name = 'report'
    readonly_fields = [
        'max_speed', 'avg_speed', 'max_accel',
        'avg_accel', 'max_alt', 'min_alt', 'normalized_alt',
        'avg_alt', 'score'
    ]
    can_delete = False


class SaqrOwnerTabularInline(admin.TabularInline):
    model = Saqr
    extra = 0
    fk_name = 'owner'


class ReportSubmittedTabularInline(admin.TabularInline):
    model = Report
    extra = 0
    fk_name = 'submitted_by'
    verbose_name = _('Submitted Report')
    verbose_name_plural = _('Submitted Reports')


class SaqrReportTabularInline(admin.TabularInline):
    model = Report
    extra = 0
    fk_name = 'saqr'
    verbose_name = _('SAQR Report')
    verbose_name_plural = _('SAQR Reports')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    inlines = [
        ReportDetailStackedAdminInline
    ]
    list_display = ['sku', 'created', 'modified']
    list_filter = [
        'show_in_public_page'
    ]

    def save_model(self, request, obj, form, change):
        obj.submitted_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            submitted_by=request.user) if not request.user.is_superuser else super().get_queryset(request)


@admin.register(ReportDetail)
class ReportDetailAdmin(admin.ModelAdmin):
    list_display = [
        'report', 'max_speed', 'avg_speed',
        'max_accel', 'avg_accel', 'max_alt', 'normalized_alt',
        'min_alt', 'avg_alt', 'score'
    ]

    readonly_fields = [
        'max_speed', 'avg_speed', 'max_accel',
        'avg_accel', 'max_alt', 'min_alt', 'normalized_alt',
        'avg_alt', 'score'
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            report__submitted_by=request.user) if not request.user.is_superuser else super().get_queryset(request)


@admin.register(SaqrImage)
class SaqrImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Saqr)
class SaqrAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'weight',
        'birth_date',
        'is_verified',
        'created',
        'modified'
    ]

    list_filter = [
        'is_verified',
        'birth_date',
        'created',
        'modified'
    ]

    filter_horizontal = ['images']

    raw_id_fields = ['owner']

    search_fields = [
        'name',
    ]

    inlines = [
        SaqrReportTabularInline
    ]

    def save_model(self, request, obj, form, change):
        obj.submitted_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            submitted_by=request.user) if not request.user.is_superuser else super().get_queryset(request)
