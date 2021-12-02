"""
Auto Generated urls.py
Automatically generated with ❤️ by django-sage-painless
"""

from rest_framework.routers import DefaultRouter

from cms.api.views import (
    AboutCompanyViewset,
    AboutTrackerViewset,
    AboutDashboardViewset,
    HowToGetCertificateViewset,
    ContactUsViewset,
    FaqViewset,
    SiteInfoViewset,

)

router = DefaultRouter()

# router.register(r'aboutcompany', AboutCompanyViewset, basename='aboutcompany')
#
# router.register(r'abouttracker', AboutTrackerViewset, basename='abouttracker')
#
# router.register(
#     r'aboutdashboard',
#     AboutDashboardViewset,
#      basename='aboutdashboard')
#
# router.register(
#     r'howtogetcertificate',
#     HowToGetCertificateViewset,
#      basename='howtogetcertificate')
#
# router.register(r'contactus', ContactUsViewset, basename='contactus')

router.register(r'faq', FaqViewset, basename='faq')

# router.register(r'siteinfo', SiteInfoViewset, basename='siteinfo')

urlpatterns = router.urls
