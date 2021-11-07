"""
Auto Generated serializers.py
Automatically generated with ❤️ by django-sage-painless
"""
from rest_framework.serializers import ModelSerializer

from cms.models.aboutcompany import AboutCompany

from cms.models.abouttracker import AboutTracker

from cms.models.aboutdashboard import AboutDashboard

from cms.models.howtogetcertificate import HowToGetCertificate

from cms.models.contactus import ContactUs

from cms.models.faq import Faq

from cms.models.siteinfo import SiteInfo


class AboutCompanySerializer(ModelSerializer):
    """
    AboutCompany Serializer
    Auto generated
    """
    class Meta:
        model = AboutCompany
        fields = [
            'id',
            'title',
            'description',
            'first_image',
            'second_image',
            'video_cover',
            'video',
            'created',
            'modified',
        
        ]


class AboutTrackerSerializer(ModelSerializer):
    """
    AboutTracker Serializer
    Auto generated
    """
    class Meta:
        model = AboutTracker
        fields = [
            'id',
            'title',
            'description',
            'image',
            'created',
            'modified',
        
        ]


class AboutDashboardSerializer(ModelSerializer):
    """
    AboutDashboard Serializer
    Auto generated
    """
    class Meta:
        model = AboutDashboard
        fields = [
            'id',
            'title',
            'description',
            'first_image',
            'second_image',
            'created',
            'modified',
        
        ]


class HowToGetCertificateSerializer(ModelSerializer):
    """
    HowToGetCertificate Serializer
    Auto generated
    """
    class Meta:
        model = HowToGetCertificate
        fields = [
            'id',
            'title',
            'description',
            'image',
            'created',
            'modified',
        
        ]


class ContactUsSerializer(ModelSerializer):
    """
    ContactUs Serializer
    Auto generated
    """
    class Meta:
        model = ContactUs
        fields = [
            'id',
            'title',
            'description',
            'tel',
            'email',
            'created',
            'modified',
        
        ]


class FaqSerializer(ModelSerializer):
    """
    Faq Serializer
    Auto generated
    """
    class Meta:
        model = Faq
        fields = [
            'id',
            'question',
            'answer',
            'created',
            'modified',
        
        ]


class SiteInfoSerializer(ModelSerializer):
    """
    SiteInfo Serializer
    Auto generated
    """
    class Meta:
        model = SiteInfo
        fields = [
            'id',
            'logo',
            'tel',
            'email',
            'address',
            'instagram',
            'facebook',
            'twitter',
            'linkedin',
            'whatsapp',
            'footer',
            'created',
            'modified',
        
        ]
