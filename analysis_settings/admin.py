from django.contrib import admin

from analysis_settings.models import Parameters


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
