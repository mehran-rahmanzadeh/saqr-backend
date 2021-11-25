from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from analysis.models.saqr_model import Saqr


class SaqrSerializer(ModelSerializer):
    """SAQR Serializer Class"""

    class Meta:
        model = Saqr
        fields = (
            'sku',
            'weight',
            'age',
            'image',
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

    class Meta:
        model = Saqr
        fields = (
            'weight',
            'age',
            'owner',
            'image',
        )
