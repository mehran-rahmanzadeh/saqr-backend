from modeltranslation.translator import register, TranslationOptions

from customer_club.models import Question


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer'
    )
