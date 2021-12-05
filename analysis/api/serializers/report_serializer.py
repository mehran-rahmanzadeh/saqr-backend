from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from analysis.api.serializers.saqr_serializer import MinimizedSaqrSerializer
from analysis.models.report_model import Report, ReportDetail
from analysis.models.saqr_model import Saqr


class ReportDetailSerializer(ModelSerializer):
    """Report Detail Serializer Class"""
    total_max_score = SerializerMethodField()
    total_min_score = SerializerMethodField()
    fundamental_score = SerializerMethodField()

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
            'normalized_alt',
            'signal_status',
            'avg_gps_count',
            'score',
            'fundamental_score',
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
            'total_max_score',
            'total_min_score',
            'created',
            'modified'
        )

    def get_total_max_score(self, obj):
        return ReportDetail.objects.order_by('-score').first().score

    def get_total_min_score(self, obj):
        return ReportDetail.objects.order_by('score').first().score

    def get_fundamental_score(self, obj):
        return obj.report.saqr.calculate_fundamental_score()


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
            'normalized_alt',
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


class MinimizedWithoutSaqrReportSerializer(ModelSerializer):
    report_detail = MinimizedReportDetailSerializer()

    class Meta:
        model = Report
        fields = (
            'report_detail',
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


class SaqrTotalSerializer(ModelSerializer):
    """Saqr Total Serializer"""
    last_report = SerializerMethodField()
    fundamental_score = SerializerMethodField()

    class Meta:
        model = Saqr
        fields = (
            'last_report',
            'fundamental_score'
        )

    def get_fundamental_score(self, obj):
        return obj.calculate_fundamental_score()

    def get_last_report(self, obj):
        return MinimizedWithoutSaqrReportSerializer(obj.reports.last()).data
