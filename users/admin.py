from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified')
    list_filter = ('is_verified', 'is_staff', 'is_active', 'last_login', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
