from rest_framework.serializers import ModelSerializer

from customer_club.models import Question


class QuestionSerializer(ModelSerializer):
    """Question Serializer Class"""

    class Meta:
        model = Question
        fields = (
            'sku',
            'question',
            'answer',
            'cover',
            'image',
            'created',
            'modified'
        )
