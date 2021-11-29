from django.urls import path

from blog.views import BlogListView

urlpatterns = [
    path('blog/list/', BlogListView.as_view(), name='blog-list')
]
