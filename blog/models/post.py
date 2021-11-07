"""
Auto Generated models.py
Automatically generated with ❤️ by django-sage-painless
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


# cache support
from blog.mixins import ModelCacheMixin


from blog.models.category import Category

from blog.models.tag import Tag


class Post(models.Model, ModelCacheMixin):
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
    
    created = models.DateTimeField(
             auto_now_add=True,
             
    )
    
    modified = models.DateTimeField(
             auto_now=True,
             
    )
    
    def __str__(self):
        return f"Post {self.pk}" 

    class Meta:
        verbose_name = _("Post")  # auto generated verbose_name
        verbose_name_plural = _("Posts")
