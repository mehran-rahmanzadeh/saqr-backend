from django.urls import path

from cms.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
