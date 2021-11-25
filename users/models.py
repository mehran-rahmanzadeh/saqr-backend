from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """User Model"""
    email = models.EmailField(_('email address'))
    first_name = models.CharField(
        _('first name'),
        max_length=150
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150
    )
    is_verified = models.BooleanField(
        _('Is Verified'),
        default=False
    )
    is_operator = models.BooleanField(
        _('Is Operator'),
        default=False
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
