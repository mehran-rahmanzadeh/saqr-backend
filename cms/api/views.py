"""
Auto Generated views.py
Automatically generated with ❤️ by django-sage-painless
"""

from django.http import Http404

from rest_framework.viewsets import ModelViewSet


from cms.models.aboutcompany import AboutCompany

from cms.models.abouttracker import AboutTracker

from cms.models.aboutdashboard import AboutDashboard

from cms.models.howtogetcertificate import HowToGetCertificate

from cms.models.contactus import ContactUs

from cms.models.faq import Faq

from cms.models.siteinfo import SiteInfo

from cms.api.serializers import (
    AboutCompanySerializer,
    AboutTrackerSerializer,
    AboutDashboardSerializer,
    HowToGetCertificateSerializer,
    ContactUsSerializer,
    FaqSerializer,
    SiteInfoSerializer,

)


class AboutCompanyViewset(ModelViewSet):
    """
    AboutCompany Viewset
    Auto generated
    """
    serializer_class = AboutCompanySerializer
    
    http_method_names = ['get']
    
    model_class = AboutCompany

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
    

class AboutTrackerViewset(ModelViewSet):
    """
    AboutTracker Viewset
    Auto generated
    """
    serializer_class = AboutTrackerSerializer
    
    http_method_names = ['get']
    
    model_class = AboutTracker

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
    

class AboutDashboardViewset(ModelViewSet):
    """
    AboutDashboard Viewset
    Auto generated
    """
    serializer_class = AboutDashboardSerializer
    
    http_method_names = ['get']
    
    model_class = AboutDashboard

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
    

class HowToGetCertificateViewset(ModelViewSet):
    """
    HowToGetCertificate Viewset
    Auto generated
    """
    serializer_class = HowToGetCertificateSerializer
    
    http_method_names = ['get']
    
    model_class = HowToGetCertificate

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
    

class ContactUsViewset(ModelViewSet):
    """
    ContactUs Viewset
    Auto generated
    """
    serializer_class = ContactUsSerializer
    
    http_method_names = ['get']
    
    model_class = ContactUs

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
    

class FaqViewset(ModelViewSet):
    """
    Faq Viewset
    Auto generated
    """
    serializer_class = FaqSerializer
    
    http_method_names = ['get']
    
    model_class = Faq

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
    

class SiteInfoViewset(ModelViewSet):
    """
    SiteInfo Viewset
    Auto generated
    """
    serializer_class = SiteInfoSerializer
    
    http_method_names = ['get']
    
    model_class = SiteInfo

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
    
