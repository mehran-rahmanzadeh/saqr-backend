from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from analysis.admin import SaqrOwnerTabularInline, ReportSubmittedTabularInline
from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_verified')
    list_filter = (
        'is_verified', 'is_operator', 'is_staff',
        'is_active', 'last_login', 'date_joined'
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_verified', 'is_operator',
                'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions',)

    inlines = [
        SaqrOwnerTabularInline,
        ReportSubmittedTabularInline
    ]
