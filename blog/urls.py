from django.urls import path

from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('blog/list/', BlogListView.as_view(), name='blog-list'),
    path('blog/detail/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail')
]
