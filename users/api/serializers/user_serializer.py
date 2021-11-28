from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'is_verified',
            'birth_date',
            'address',
            'date_joined'
        )
        read_only_fields = (
            'date_joined',
            'is_verified'
        )
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False}
        }
