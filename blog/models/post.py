"""
Auto Generated models.py
Automatically generated with ❤️ by django-sage-painless
"""
import secrets

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


# cache support
from blog.mixins import ModelCacheMixin


from blog.models.category import Category

from blog.models.tag import Tag

from painless.utils.models.mixins import Sku_Mixin


class Post(Sku_Mixin, ModelCacheMixin):
    """
    Post Model
    Auto generated
    """
    
    CACHE_KEY = 'post'  # auto generated CACHE_KEY
    
    kind = models.CharField(
             max_length=10,
             choices=[['image', 'Image Article'], ['video', 'Video Article']],
             
    )
    
    title = models.CharField(
             max_length=255,
             
    )

    slug = models.SlugField(
        max_length=255
    )
    
    body = models.TextField(
             
    )
    
    image = models.ImageField(
             null=True,
             blank=True,
             
    )
    
    video_cover = models.ImageField(
             null=True,
             blank=True,
             
    )
    
    video = models.FileField(
             null=True,
             blank=True,
             
    )
    
    category = models.ForeignKey(
             to=Category,
             on_delete=models.CASCADE,
             
    )
    
    tags = models.ManyToManyField(
             to=Tag,
             blank=True,
             
    )

    show_in_index = models.BooleanField(
        default=True
    )
    
    created = models.DateTimeField(
             auto_now_add=True,
             
    )
    
    modified = models.DateTimeField(
             auto_now=True,
             
    )
    
    def __str__(self):
        return f"Post {self.pk}" 
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'post-{secrets.token_urlsafe(8)}'
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Post")  # auto generated verbose_name
        verbose_name_plural = _("Posts")
