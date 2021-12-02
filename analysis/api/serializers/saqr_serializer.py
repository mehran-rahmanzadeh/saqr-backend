from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from analysis.models.saqr_model import Saqr, SaqrImage


class SaqrImageSerializer(ModelSerializer):
    """SAQR Image Serializer Class"""
    class Meta:
        model = SaqrImage
        fields = (
            'sku',
            'image',
        )
        read_only_fields = (
            'sku',
        )


class SaqrSerializer(ModelSerializer):
    """SAQR Serializer Class"""
    images = SaqrImageSerializer(many=True, required=False)

    class Meta:
        model = Saqr
        fields = (
            'sku',
            'title',
            'weight',
            'age',
            'images',
            'passport_image',
            'profile_image',
            'cover',
            'owner',
            'is_verified',
            'created',
            'modified'
        )
        read_only_fields = (
            'sku',
            'is_verified',
            'images',
            'created',
            'modified'
        )


class SaqrOwnerSerializer(ModelSerializer):
    """SAQR Owner Serializer"""

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name'
        )


class MinimizedSaqrSerializer(ModelSerializer):
    """Minimized SAQR Serializer"""
    owner = SaqrOwnerSerializer()

    class Meta:
        model = Saqr
        fields = (
            'title',
            'weight',
            'age',
            'owner',
            'profile_image'
        )
