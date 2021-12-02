from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from analysis.models.saqr_model import Saqr


@receiver(post_save, sender=get_user_model())
def user_post_save(sender, instance, created, **kwargs):
    """user post save"""
    if created:
        Saqr.objects.create(
            owner=instance
        )
