"""
Auto Generated serializers.py
Automatically generated with ❤️ by django-sage-painless
"""
from rest_framework.serializers import ModelSerializer

from calls.models.getintouch import GetInTouch

from calls.models.certificaterequest import CertificateRequest


class GetInTouchSerializer(ModelSerializer):
    """
    GetInTouch Serializer
    Auto generated
    """
    class Meta:
        model = GetInTouch
        fields = [
            'id',
            'name',
            'email',
            'subject',
            'phone',
            'message',
            'seen',
            'created',
            'modified',
        
        ]


class CertificateRequestSerializer(ModelSerializer):
    """
    CertificateRequest Serializer
    Auto generated
    """
    class Meta:
        model = CertificateRequest
        fields = [
            'id',
            'email',
            'seen',
            'created',
            'modified',
        
        ]
