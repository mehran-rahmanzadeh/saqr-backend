from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

from authentication.tasks import send_mail


class ResetPasswordTokenHelper:
    """Reset password tokens helper"""

    @classmethod
    def get_token_generator(cls):
        return default_token_generator

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
