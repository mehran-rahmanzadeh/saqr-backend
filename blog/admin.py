"""
Auto Generated admin.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.contrib import admin

from blog.models.tag import Tag

from blog.models.category import Category

from blog.models.post import Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Tag Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    list_filter = ['created', 'modified']

    search_fields = ['title']

    fieldsets = (
        (None, {
            'fields': (
                'title_en', 'title_ar'
            )
        }),
    )

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    list_filter = ['created', 'modified']

    search_fields = ['title']

    fieldsets = (
        (None, {
            'fields': (
                'title_en', 'title_ar'
            )
        }),
    )

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post Admin
    Auto generated
    """
    list_display = ['title', 'created', 'modified']

    list_filter = ['created', 'modified']

    search_fields = ['title', 'body']

    fieldsets = (
        (None, {
            'fields': (
                'title_en', 'title_ar',
                'body_en', 'body_ar'
            )
        }),
    )

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True
