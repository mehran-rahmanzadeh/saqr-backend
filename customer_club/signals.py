from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from customer_club.models import Notification, UserNotification
from customer_club.tasks import send_email_to_users


@receiver(m2m_changed, sender=Notification.users.through)
def notification_post_save(sender, instance, *args, **kwargs):
    """create UserNotification instances
    send email if needed
    """
    users = instance.users.all()

    # create UserNotification objs
    user_notification_objects = [
        UserNotification(
            user=user,
            notification=instance
        ) for user in users
    ]
    UserNotification.objects.bulk_create(user_notification_objects)

    # send mail
    if instance.send_email:
        emails = users.values_list('email', flat=True)
        send_email_to_users.delay(list(emails), instance.subject, instance.body)
