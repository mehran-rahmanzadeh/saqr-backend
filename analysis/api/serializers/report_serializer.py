from rest_framework.serializers import ModelSerializer

from analysis.api.serializers.saqr_serializer import MinimizedSaqrSerializer
from analysis.models.report_model import Report, ReportDetail


class ReportDetailSerializer(ModelSerializer):
    """Report Detail Serializer Class"""

    class Meta:
        model = ReportDetail
        fields = (
            'max_speed',
            'avg_speed',
            'max_accel',
            'avg_accel',
            'max_alt',
            'avg_alt',
            'min_alt',
            'signal_status',
            'avg_gps_count',
            'score',
            'lon_array',
            'lat_array',
            'alt_array',
            'speed_array',
            'accel_array',
            'timestamp_array',
            'sep_array',
            'track_array',
            'utc_array',
            'sip_array',
            'fix_array',
            'sv_array',
            'status_array',
            'quality_array',
            'created',
            'modified'
        )


class MinimizedReportDetailSerializer(ModelSerializer):
    class Meta:
        model = ReportDetail
        fields = (
            'max_speed',
            'avg_speed',
            'max_accel',
            'avg_accel',
            'max_alt',
            'avg_alt',
            'signal_status',
            'avg_gps_count',
            'score',
        )


class MinimizedReportSerializer(ModelSerializer):
    report_detail = MinimizedReportDetailSerializer()
    saqr = MinimizedSaqrSerializer()

    class Meta:
        model = Report
        fields = (
            'report_detail',
            'saqr',
        )


class ReportSerializer(ModelSerializer):
    """Report Serializer Class"""
    report_detail = ReportDetailSerializer()

    class Meta:
        model = Report
        fields = (
            'sku',
            'nmea_file',
            'report_detail'
        )
