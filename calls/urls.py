from django.urls import path

from calls.views import ContactView, CertificateRequestView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('certificate/', CertificateRequestView.as_view(), name='certificate')
]
