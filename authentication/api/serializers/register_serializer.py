from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class RegisterSerializer(ModelSerializer):
    """Register User Serializer Class"""

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        )
