from celery import shared_task

from django.core.mail import EmailMessage


@shared_task
def send_mail(email, subject, message):
    """send email"""
    mail = EmailMessage(subject, message, to=[email])
    mail.send()
