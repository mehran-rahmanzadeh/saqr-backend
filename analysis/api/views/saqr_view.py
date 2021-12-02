from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from analysis.api.serializers.report_serializer import ReportSerializer
from analysis.api.serializers.saqr_serializer import SaqrSerializer, SaqrImageSerializer


class SaqrViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin):
    """Saqr Viewset"""
    serializer_class = SaqrSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'sku'

    def get_queryset(self):
        return self.request.user.saqrs.all()

    def create(self, request, *args, **kwargs):
        payload = request.data
        payload['owner'] = request.user.pk  # set as current user
        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(serializer_class=SaqrImageSerializer, methods=['patch'], detail=True)
    def add_image(self, *args, **kwargs):
        """add image to saqr profile"""
        obj = self.get_object()
        user = self.request.user
        payload = self.request.data
        serializer = self.get_serializer(data=payload)
        if serializer.is_valid():
            if obj.owner == user:
                image = serializer.save()
                obj.images.add(image)
                response = {
                    'message': 'Image added successfully.'
                }
                code = status.HTTP_202_ACCEPTED
            else:
                response = {
                    'message': 'You do not have access to edit falcon.'
                }
                code = status.HTTP_403_FORBIDDEN
        else:
            response = serializer.errors
            code = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=code
        )

    @action(methods=['delete'], detail=True)
    def remove_image(self, *args, **kwargs):
        """remove image from saqr profile"""
        obj = self.get_object()
        user = self.request.user
        payload = self.request.data

        if obj.owner == user:
            obj.images.filter(sku=payload.get('image')).delete()
            response = {
                'message': 'Image deleted successfully.'
            }
            code = status.HTTP_202_ACCEPTED
        else:
            response = {
                'message': 'You do not have access to edit this falcon.'
            }
            code = status.HTTP_403_FORBIDDEN

        return Response(
            data=response,
            status=code
        )

    @action(serializer_class=ReportSerializer, methods=['get'], detail=True)
    def reports(self, *args, **kwargs):
        """reports action"""
        saqr = self.get_object()
        reports = saqr.reports.all()
        serializer = self.get_serializer(reports, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
