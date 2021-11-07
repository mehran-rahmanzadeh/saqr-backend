"""
Auto Generated serializers.py
Automatically generated with ❤️ by django-sage-painless
"""
from rest_framework.serializers import ModelSerializer

from blog.models.tag import Tag

from blog.models.category import Category

from blog.models.post import Post


class TagSerializer(ModelSerializer):
    """
    Tag Serializer
    Auto generated
    """

    class Meta:
        model = Tag
        fields = [
            'id',
            'title',
            'created',
            'modified',

        ]


class CategorySerializer(ModelSerializer):
    """
    Category Serializer
    Auto generated
    """

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'modified',

        ]


class PostSerializer(ModelSerializer):
    """
    Post Serializer
    Auto generated
    """
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'kind',
            'title',
            'body',
            'image',
            'video_cover',
            'video',
            'category',
            'tags',
            'created',
            'modified',

        ]
