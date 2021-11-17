from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class LoginSerializer(ModelSerializer):
    """Login User Serializer Class"""
    username = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
        )
