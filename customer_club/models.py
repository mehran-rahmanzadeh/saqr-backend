import secrets

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from painless.utils.models.mixins import TimeStampModelMixin, Sku_Mixin


class Category(Sku_Mixin, TimeStampModelMixin):
    """Category model"""
    title = models.CharField(
        _('Title'),
        max_length=255
    )

    description = models.CharField(
        _('Description'),
        max_length=255,
        null=True,
        blank=True
    )

    image = models.ImageField(
        _('Image'),
        upload_to='customer-club-category-images/',
        validators=[
            FileExtensionValidator(['png', 'PNG'])
        ],
        null=True,
        blank=True
    )

    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Category {self.title}'

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'category-{secrets.token_urlsafe(8)}'
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Question(Sku_Mixin, TimeStampModelMixin):
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question = models.CharField(
        _('Question'),
        max_length=255
    )

    answer = models.TextField(_('Answer'))

    def __str__(self):
        return f'Question {self.question}'
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'question-{secrets.token_urlsafe(8)}'
        super(Question, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
