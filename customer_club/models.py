import secrets

from django.contrib.auth import get_user_model
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


class Notification(TimeStampModelMixin):
    """Notification model"""
    users = models.ManyToManyField(
        get_user_model(),
        verbose_name=_('Users'),
        related_name='base_notifications'
    )

    send_email = models.BooleanField(
        _('Send Email'),
        default=True
    )

    subject = models.CharField(
        _('Subject'),
        max_length=255
    )

    body = models.TextField(_('Body'))

    image = models.ImageField(
        _('Image'),
        help_text=_('NOTE: can be empty'),
        null=True,
        blank=True,
        upload_to='notification-images/'
    )

    def __str__(self):
        return f'Notification {self.id}'

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
        ordering = ('-created',)


class UserNotification(Sku_Mixin, TimeStampModelMixin):
    """User Notification model"""
    user = models.ForeignKey(
        get_user_model(),
        related_name='notifications',
        on_delete=models.CASCADE
    )

    notification = models.ForeignKey(
        Notification,
        related_name='user_notifs',
        on_delete=models.CASCADE
    )

    is_seen = models.BooleanField(
        _('Is Seen By User'),
        default=False
    )

    def __str__(self):
        return f'Notification for user {self.user}'
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'notif-{secrets.token_urlsafe(8)}'
        super(UserNotification, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('User Notification')
        verbose_name_plural = _('User Notifications')
        ordering = ('-created',)
