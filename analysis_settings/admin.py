from django.contrib import admin

from analysis_settings.models import Parameters, AnalyseReview


@admin.register(Parameters)
class ParametersModelAdmin(admin.ModelAdmin):
    list_display = ['created', 'modified']

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser and not self.model.objects.exists()


@admin.register(AnalyseReview)
class AnalyseReviewModelAdmin(admin.ModelAdmin):
    list_display = ['submitted_by', 'reason', 'created']

    filter_horizontal = ['reports']

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.submitted_by = request.user
        super().save_model(request, obj, form, change)
