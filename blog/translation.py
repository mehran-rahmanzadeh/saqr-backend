from modeltranslation.translator import register, TranslationOptions

from blog.models.category import Category
from blog.models.post import Post
from blog.models.tag import Tag


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'body',
    )
