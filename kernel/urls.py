"""kernel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Rest API Doc",
        default_version='v1',
        description="Auto Generated API Docs",
        license=openapi.License(name="S.A.G.E License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('sos7243/postgres-metrics/', include('postgres_metrics.urls')),
    path('sos7243/docs/', include('django.contrib.admindocs.urls')),
    path('sos7243/', admin.site.urls, name='admin'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/v1/', include('cms.api.urls')),
    path('api/v1/', include('calls.api.urls')),
    path('api/v1/', include('blog.api.urls')),
    path('api/v1/', include('analysis.api.urls')),
    path('api/v1/', include('authentication.api.urls')),
    path('api/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin
admin.site.site_header = _('SAQR Startup')
admin.site.index_title = _('Administration')
admin.site.site_title = _('SAQR Admin')
