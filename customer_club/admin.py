from django.contrib import admin

from customer_club.models import Category, Question


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'created', 'modified']
    list_filter = ['created', 'modified']
    search_fields = ['title', 'description']

    fieldsets = (
        (None, {
            'fields': (
                'title_en', 'title_ar',
                'description_en', 'description_ar',
                'image', 'parent'
            )
        }),
    )


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'created', 'modified']
    list_filter = ['created', 'modified']
    search_fields = ['question', 'answer']
    raw_id_fields = ['category']

    fieldsets = (
        (None, {
            'fields': (
                'question_en', 'question_ar',
                'answer_en', 'answer_ar',
                'category'
            )
        }),
    )
