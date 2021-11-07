"""
Auto Generated admin.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.contrib import admin

from cms.models.aboutcompany import AboutCompany

from cms.models.abouttracker import AboutTracker

from cms.models.aboutdashboard import AboutDashboard

from cms.models.howtogetcertificate import HowToGetCertificate

from cms.models.contactus import ContactUs

from cms.models.faq import Faq

from cms.models.siteinfo import SiteInfo


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    """
    AboutCompany Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    search_fields = ['title', 'description']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(AboutTracker)
class AboutTrackerAdmin(admin.ModelAdmin):
    """
    AboutTracker Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    search_fields = ['title', 'description']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(AboutDashboard)
class AboutDashboardAdmin(admin.ModelAdmin):
    """
    AboutDashboard Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    search_fields = ['title', 'description']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(HowToGetCertificate)
class HowToGetCertificateAdmin(admin.ModelAdmin):
    """
    HowToGetCertificate Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    search_fields = ['title', 'description']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    ContactUs Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    search_fields = ['title', 'description']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    """
    Faq Admin
    Auto generated
    """
    list_display = ['question', 'created', 'modified']

    search_fields = ['question', 'answer']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    """
    SiteInfo Admin
    Auto generated
    """
    list_display = ['tel', 'email', 'created', 'modified']

    list_filter = ['created', 'modified']

    search_fields = ['tel', 'email']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True
