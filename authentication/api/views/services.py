import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache

from authentication.tasks import send_mail


class TokenGenerator:
    user_unique_attr = 'username'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def __save_token_to_cache(cls, key, token):
        """save given token to cache"""
        cache.set(key, token, timeout=settings.RESET_PASSWORD_TOKEN_TIMEOUT)

    @classmethod
    def __get_token_from_cache(cls, key):
        """get token from cache if exists"""
        return cache.get(key) or None

    @classmethod
    def __get_user_unique_attribute(cls, user: get_user_model()):
        """get attr from user obj"""
        return getattr(user, cls.user_unique_attr)

    @classmethod
    def make_token(cls, user: get_user_model()):
        """generate random token for user"""
        token = f'{random.randint(100000, 999999)}'
        cls.__save_token_to_cache(cls.__get_user_unique_attribute(user), token)
        return token

    @classmethod
    def check_token(cls, user: get_user_model(), token: str):
        """check token validation"""
        from_cache = cls.__get_token_from_cache(cls.__get_user_unique_attribute(user))
        if from_cache:
            return from_cache == token
        return False


class ResetPasswordTokenHelper:
    """Reset password tokens helper"""

    @classmethod
    def get_token_generator(cls):
        return TokenGenerator

    @classmethod
    def get_random_token(cls, user: get_user_model()):
        """generated random token for reset password"""
        return cls.get_token_generator().make_token(user=user)

    @classmethod
    def validate_token(cls, user: get_user_model(), token: str):
        """validate token for user"""
        return cls.get_token_generator().check_token(user=user, token=token)


class EmailHelper:
    @classmethod
    def create_reset_password_email_subject(cls):
        return 'Reset Password Email'

    @classmethod
    def create_reset_password_email_body(cls, token: str):
        return f'Your reset password token is {token}. Use it to recover your password.'

    @classmethod
    def send_reset_password_email(cls, user: get_user_model(), token: str):
        """send reset password email for user"""
        subject = cls.create_reset_password_email_subject()
        message = cls.create_reset_password_email_body(token)
        send_mail.delay(user.email, subject, message)
