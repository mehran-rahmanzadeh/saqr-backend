from rest_framework.serializers import ModelSerializer

from customer_club.models import Category


class CategorySerializer(ModelSerializer):
    """Category Serializer Class"""

    class Meta:
        model = Category
        fields = (
            'sku',
            'title',
            'description',
            'image'
        )
