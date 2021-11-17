from rest_framework.routers import DefaultRouter

from analysis.api.views.report_view import ReportViewset
from analysis.api.views.saqr_view import SaqrViewset

router = DefaultRouter()
router.register(r'saqrs', SaqrViewset, basename='saqrs')
router.register(r'reports', ReportViewset, basename='reports')

urlpatterns = router.urls
