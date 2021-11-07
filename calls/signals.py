"""
Auto Generated signals.py
Automatically generated with ❤️ by django-sage-painless
"""

from django.db.models import signals


from calls.models.getintouch import GetInTouch

from calls.models.certificaterequest import CertificateRequest

from calls.services import clear_cache_for_model


def getintouch_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(getintouch_clear_cache, sender=GetInTouch)
signals.pre_delete.connect(getintouch_clear_cache, sender=GetInTouch)


def certificaterequest_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(
    certificaterequest_clear_cache,
     sender=CertificateRequest)
signals.pre_delete.connect(
    certificaterequest_clear_cache,
     sender=CertificateRequest)
