from modeltranslation.translator import register, TranslationOptions

from customer_club.models import Category, Question


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer'
    )
