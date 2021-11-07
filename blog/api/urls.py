"""
Auto Generated urls.py
Automatically generated with ❤️ by django-sage-painless
"""

from rest_framework.routers import DefaultRouter

from blog.api.views import (
    TagViewset,
    CategoryViewset,
    PostViewset,

)

router = DefaultRouter()

router.register(r'tag', TagViewset, basename='tag')

router.register(r'category', CategoryViewset, basename='category')

router.register(r'post', PostViewset, basename='post')

urlpatterns = router.urls
