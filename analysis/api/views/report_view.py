from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from analysis.api.serializers.report_serializer import ReportSerializer
from analysis.models.report_model import Report


class ReportViewset(GenericViewSet, RetrieveModelMixin):
    """Report Viewset"""
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all()
    lookup_field = 'sku'
