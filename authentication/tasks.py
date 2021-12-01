from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail as django_send_mail


@shared_task
def send_mail(email, subject, message):
    """send email"""
    if email:
        django_send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
