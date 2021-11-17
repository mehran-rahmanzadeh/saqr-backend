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
            'is_verified',
            'created',
            'modified'
        )
