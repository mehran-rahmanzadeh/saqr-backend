from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from customer_club.api.serializers.question_serializer import QuestionSerializer
from customer_club.models import Question


class QuestionViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Question Viewset"""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'sku'
    filter_backends = [SearchFilter]
    search_fields = [
        'question',
        'answer'
    ]
