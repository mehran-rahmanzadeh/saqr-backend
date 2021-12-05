from django.conf import settings
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from analysis.api.serializers.report_serializer import (
    ReportSerializer,
    MinimizedReportSerializer
)
from analysis.models.report_model import Report


class ReportViewset(GenericViewSet, RetrieveModelMixin):
    """Report Viewset"""
    serializer_class = ReportSerializer
    permission_classes = (AllowAny,)
    queryset = Report.objects.select_related('report_detail')
    lookup_field = 'sku'


class TotalReportViewset(GenericViewSet, ListModelMixin):
    """Total Report Viewset"""
    serializer_class = MinimizedReportSerializer
    permission_classes = (AllowAny,)
    queryset = Report.objects.filter(show_in_public_page=True).select_related('saqr', 'report_detail')
    filter_backends = [OrderingFilter]
    ordering_fields = (
        'report_detail__max_speed',
        'report_detail__avg_speed',
        'report_detail__max_accel',
        'report_detail__avg_accel',
        'report_detail__max_alt',
        'report_detail__avg_alt',
        'report_detail__normalized_alt',
        'report_detail__score'
    )

    def finalize_response(self, request, response, *args, **kwargs):
        """limit number of instances showing in public response"""
        limit_response_count = settings.LIMIT_PUBLIC_REPORT_COUNT
        response.data['count'] = limit_response_count if response.data['count'] > limit_response_count else response.data['count']
        response.data['results'] = response.data['results'][:limit_response_count]
        return super().finalize_response(request, response, *args, **kwargs)
