"""
Auto Generated urls.py
Automatically generated with ❤️ by django-sage-painless
"""

from rest_framework.routers import DefaultRouter

from calls.api.views import (
    GetInTouchViewset,
    CertificateRequestViewset,

)

router = DefaultRouter()

# router.register(r'getintouch', GetInTouchViewset, basename='getintouch')

router.register(
    r'certificaterequest',
    CertificateRequestViewset,
     basename='certificaterequest')

urlpatterns = router.urls
