from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()
