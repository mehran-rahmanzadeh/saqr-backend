from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from analysis.api.serializers.report_serializer import ReportSerializer
from analysis.api.serializers.saqr_serializer import SaqrSerializer


class SaqrViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Saqr Viewset"""
    serializer_class = SaqrSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'sku'

    def get_queryset(self):
        return self.request.user.saqrs.all()

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
