from modeltranslation.translator import register, TranslationOptions

from cms.models.aboutcompany import AboutCompany
from cms.models.aboutdashboard import AboutDashboard
from cms.models.abouttest import AboutTest
from cms.models.abouttracker import AboutTracker
from cms.models.contactus import ContactUs
from cms.models.faq import Faq
from cms.models.howtogetcertificate import HowToGetCertificate
from cms.models.siteinfo import SiteInfo


@register(AboutCompany)
class AboutCompanyTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


@register(AboutDashboard)
class AboutDashboardTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


@register(AboutTest)
class AboutTestTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


@register(AboutTracker)
class AboutTrackerTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


@register(ContactUs)
class ContactUsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer'
    )


@register(HowToGetCertificate)
class HowToGetCertificateTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


@register(SiteInfo)
class SiteInfoTranslationOptions(TranslationOptions):
    fields = (
        'address',
        'footer'
    )
