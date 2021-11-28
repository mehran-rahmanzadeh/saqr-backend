from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_email_to_users(users_emails, subject, body):
    """send email to user"""
    mail = EmailMessage(subject, body, to=users_emails)
    mail.send()
