from django.contrib import admin

from customer_club.models import Question, Notification


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'created', 'modified']
    list_filter = ['created', 'modified']
    search_fields = ['question', 'answer']

    fieldsets = (
        (None, {
            'fields': (
                'question_en', 'question_ar',
                'answer_en', 'answer_ar',
                'cover', 'image'
            )
        }),
    )


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created', 'modified']
    list_filter = ['created', 'modified']
    search_fields = ['subject', 'body']
    filter_horizontal = ['users']
