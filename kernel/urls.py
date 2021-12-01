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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from rest_framework.permissions import AllowAny

urlpatterns = i18n_patterns(
    # admin
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('gt86/postgres-metrics/', include('postgres_metrics.urls')),
    path('gt86/docs/', include('django.contrib.admindocs.urls')),
    path('gt86/', admin.site.urls, name='admin'),

    # API
    path('i18n/', include('django.conf.urls.i18n')),
    # path('api/v1/', include('cms.api.urls')),
    path('api/v1/', include('calls.api.urls')),
    # path('api/v1/', include('blog.api.urls')),
    path('api/v1/', include('analysis.api.urls')),
    path('api/v1/', include('authentication.api.urls')),
    path('api/v1/', include('users.api.urls')),
    path('api/v1/', include('customer_club.api.urls')),
    # path('api/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),

    # mvt pages
    path('', include('cms.urls')),
    path('', include('calls.urls')),
    path('', include('blog.urls')),

    # debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),

) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin
admin.site.site_header = _('SAQR Startup')
admin.site.index_title = _('Administration')
admin.site.site_title = _('SAQR Admin')
