from rest_framework import serializers


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField()
