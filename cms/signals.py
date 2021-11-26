"""
Auto Generated signals.py
Automatically generated with ❤️ by django-sage-painless
"""

from django.db.models import signals

from cms.models.aboutcompany import AboutCompany

from cms.models.abouttest import AboutTest

from cms.models.abouttracker import AboutTracker

from cms.models.aboutdashboard import AboutDashboard

from cms.models.howtogetcertificate import HowToGetCertificate

from cms.models.contactus import ContactUs

from cms.models.faq import Faq

from cms.models.siteinfo import SiteInfo

from cms.services import clear_cache_for_model


def aboutcompany_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(aboutcompany_clear_cache, sender=AboutCompany)
signals.pre_delete.connect(aboutcompany_clear_cache, sender=AboutCompany)


def abouttracker_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(abouttracker_clear_cache, sender=AboutTracker)
signals.pre_delete.connect(abouttracker_clear_cache, sender=AboutTracker)


def aboutdashboard_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(aboutdashboard_clear_cache, sender=AboutDashboard)
signals.pre_delete.connect(aboutdashboard_clear_cache, sender=AboutDashboard)


def howtogetcertificate_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(
    howtogetcertificate_clear_cache,
    sender=HowToGetCertificate)
signals.pre_delete.connect(
    howtogetcertificate_clear_cache,
    sender=HowToGetCertificate)


def contactus_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(contactus_clear_cache, sender=ContactUs)
signals.pre_delete.connect(contactus_clear_cache, sender=ContactUs)


def faq_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(faq_clear_cache, sender=Faq)
signals.pre_delete.connect(faq_clear_cache, sender=Faq)


def siteinfo_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(siteinfo_clear_cache, sender=SiteInfo)
signals.pre_delete.connect(siteinfo_clear_cache, sender=SiteInfo)


def abouttest_clear_cache(sender, **kwargs):
    clear_cache_for_model(sender.CACHE_KEY)


signals.post_save.connect(aboutcompany_clear_cache, sender=AboutTest)
signals.pre_delete.connect(aboutcompany_clear_cache, sender=AboutTest)
