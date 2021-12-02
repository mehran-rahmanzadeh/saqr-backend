import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from painless.utils.models.mixins import TimeStampModelMixin, Sku_Mixin


class Question(Sku_Mixin, TimeStampModelMixin):
    cover = models.ImageField(
        _('Cover'),
        upload_to='question-covers/',
        null=True,
        blank=True
    )

    image = models.ImageField(
        _('Image'),
        upload_to='question-images/',
        null=True,
        blank=True
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
