from django.shortcuts import redirect
from django.views import View

from calls.models.certificaterequest import CertificateRequest
from calls.models.getintouch import GetInTouch


class ContactView(View):

    def post(self, *args, **kwargs):
        data = self.request.POST
        GetInTouch.objects.create(**data)
        return redirect('index')


class CertificateRequestView(View):

    def post(self, *args, **kwargs):
        data = self.request.POST
        CertificateRequest.objects.create(**data)
        return redirect('index')
