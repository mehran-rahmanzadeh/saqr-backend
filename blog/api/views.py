"""
Auto Generated views.py
Automatically generated with ❤️ by django-sage-painless
"""

from django.http import Http404

from rest_framework.viewsets import ModelViewSet


# filter support
from django_filters.rest_framework import DjangoFilterBackend


# search support
from rest_framework.filters import SearchFilter


from blog.models.tag import Tag

from blog.models.category import Category

from blog.models.post import Post

from blog.api.serializers import (
    TagSerializer,
    CategorySerializer,
    PostSerializer,

)


class TagViewset(ModelViewSet):
    """
    Tag Viewset
    Auto generated
    """
    serializer_class = TagSerializer
    
    http_method_names = ['get']
    
    model_class = Tag

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {
            self.lookup_field: int(
                self.kwargs[lookup_url_kwarg]) if self.kwargs[lookup_url_kwarg].isdigit() else None
        }
        qs = self.model_class.filter_from_cache(queryset, **filter_kwargs)
        if len(qs) == 0:
            raise Http404('Not Found')
        obj = qs[0]
        return obj
    

class CategoryViewset(ModelViewSet):
    """
    Category Viewset
    Auto generated
    """
    serializer_class = CategorySerializer
    
    http_method_names = ['get']
    
    model_class = Category

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {
            self.lookup_field: int(
                self.kwargs[lookup_url_kwarg]) if self.kwargs[lookup_url_kwarg].isdigit() else None
        }
        qs = self.model_class.filter_from_cache(queryset, **filter_kwargs)
        if len(qs) == 0:
            raise Http404('Not Found')
        obj = qs[0]
        return obj
    

class PostViewset(ModelViewSet):
    """
    Post Viewset
    Auto generated
    """
    serializer_class = PostSerializer
    
    http_method_names = ['get']
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        'title', 'body', 'created', 'modified',
    ]
    filterset_fields = [
        'kind', 'title', 'body', 'category__id', 'tags__id', 'created', 'modified',
    ]
    
    model_class = Post

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {
            self.lookup_field: int(
                self.kwargs[lookup_url_kwarg]) if self.kwargs[lookup_url_kwarg].isdigit() else None
        }
        qs = self.model_class.filter_from_cache(queryset, **filter_kwargs)
        if len(qs) == 0:
            raise Http404('Not Found')
        obj = qs[0]
        return obj
    
