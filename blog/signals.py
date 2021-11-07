"""
Auto Generated signals.py
Automatically generated with ❤️ by django-sage-painless
"""

from django.db.models import signals


from blog.models.tag import Tag

from blog.models.category import Category

from blog.models.post import Post

from blog.services import clear_cache_for_model


def tag_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(tag_clear_cache, sender=Tag)
signals.pre_delete.connect(tag_clear_cache, sender=Tag)


def category_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(category_clear_cache, sender=Category)
signals.pre_delete.connect(category_clear_cache, sender=Category)


def post_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(post_clear_cache, sender=Post)
signals.pre_delete.connect(post_clear_cache, sender=Post)
