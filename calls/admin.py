"""
Auto Generated admin.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.contrib import admin

from calls.models.getintouch import GetInTouch

from calls.models.certificaterequest import CertificateRequest


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    """
    GetInTouch Admin
    Auto generated
    """
    list_display = ['subject', 'name', 'email', 'seen', 'created', 'modified']

    list_filter = ['created', 'modified', 'seen']

    search_fields = ['subject', 'name', 'message', 'email', 'phone']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(CertificateRequest)
class CertificateRequestAdmin(admin.ModelAdmin):
    """
    CertificateRequest Admin
    Auto generated
    """
    list_display = ['email', 'seen', 'created', 'modified']

    list_filter = ['created', 'modified', 'seen']

    search_fields = ['email']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True
