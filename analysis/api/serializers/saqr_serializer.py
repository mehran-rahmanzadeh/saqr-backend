from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from analysis.models.saqr_model import Saqr, SaqrImage


class SaqrImageSerializer(ModelSerializer):
    """SAQR Image Serializer Class"""
    class Meta:
        model = SaqrImage
        fields = (
            'image',
        )


class SaqrSerializer(ModelSerializer):
    """SAQR Serializer Class"""
    images = SaqrImageSerializer(many=True)

    class Meta:
        model = Saqr
        fields = (
            'sku',
            'weight',
            'age',
            'images',
            'passport_image',
            'is_verified',
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
    image = SerializerMethodField()

    class Meta:
        model = Saqr
        fields = (
            'weight',
            'age',
            'owner',
            'image'
        )

    def get_image(self, obj):
        return SaqrImageSerializer(obj.images.first()).data
