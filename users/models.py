from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from painless.utils.regex.patterns import INTERNATIONAL_PHONE_NUMBER_PATTERN


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
    phone_number = models.CharField(
        _('Phone Number'),
        null=True,
        blank=True,
        max_length=15,
        validators=[
            RegexValidator(INTERNATIONAL_PHONE_NUMBER_PATTERN)
        ]
    )
    address = models.TextField(
        _('Address'),
        null=True,
        blank=True
    )
    birth_date = models.DateField(
        _('Birth Date'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
