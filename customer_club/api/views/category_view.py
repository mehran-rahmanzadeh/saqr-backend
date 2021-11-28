from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from customer_club.api.serializers.category_serializer import CategorySerializer
from customer_club.models import Category


class CategoryViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Category Viewset"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'sku'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'parent__sku'
    ]

    @action(detail=False, methods=['get'])
    def parents(self, *args, **kwargs):
        queryset = Category.objects.filter(parent__isnull=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
