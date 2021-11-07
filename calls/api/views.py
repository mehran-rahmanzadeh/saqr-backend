"""
Auto Generated views.py
Automatically generated with ❤️ by django-sage-painless
"""

from django.http import Http404

from rest_framework.viewsets import ModelViewSet


from calls.models.getintouch import GetInTouch

from calls.models.certificaterequest import CertificateRequest

from calls.api.serializers import (
    GetInTouchSerializer,
    CertificateRequestSerializer,

)


class GetInTouchViewset(ModelViewSet):
    """
    GetInTouch Viewset
    Auto generated
    """
    serializer_class = GetInTouchSerializer
    
    http_method_names = ['post']
    
    model_class = GetInTouch

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {
            self.lookup_field: int(
                self.kwargs[lookup_url_kwarg]) if self.kwargs[lookup_url_kwarg].isdigit() else None
        }
        qs = self.model_class.filter_from_cache(queryset, **filter_kwargs)
        if len(qs) == 0:
            raise Http404('Not Found')
        obj = qs[0]
        return obj
    

class CertificateRequestViewset(ModelViewSet):
    """
    CertificateRequest Viewset
    Auto generated
    """
    serializer_class = CertificateRequestSerializer
    
    http_method_names = ['post']
    
    model_class = CertificateRequest

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {
            self.lookup_field: int(
                self.kwargs[lookup_url_kwarg]) if self.kwargs[lookup_url_kwarg].isdigit() else None
        }
        qs = self.model_class.filter_from_cache(queryset, **filter_kwargs)
        if len(qs) == 0:
            raise Http404('Not Found')
        obj = qs[0]
        return obj
    
