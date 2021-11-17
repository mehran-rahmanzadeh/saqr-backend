from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.api.serializers.reset_password_serializer import (
    ResetPasswordSerializer,
    VerifyResetPasswordSerializer
)
from authentication.api.views.services import ResetPasswordTokenHelper, EmailHelper


class SendResetPasswordToken(APIView):
    """Send Reset Password Token API View"""
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, *args, **kwargs):
        payload = self.request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            user = get_user_model().objects.filter(email=payload.get('email'))
            if user.exists():
                user = user.first()
                if user.is_active:
                    token = ResetPasswordTokenHelper.get_random_token(user=user)
                    EmailHelper.send_reset_password_email(user=user, token=token)
                    response = {
                        'message': 'Reset password token sent to your email.'
                    }
                    code = status.HTTP_202_ACCEPTED
                else:
                    response = {
                        'message': 'Account is not active.'
                    }
                    code = status.HTTP_403_FORBIDDEN
            else:
                response = {
                    'message': 'User not found.'
                }
                code = status.HTTP_404_NOT_FOUND
        else:
            response = serializer.errors
            code = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=code
        )


class VerifyResetPasswordTokenAPIView(APIView):
    """Verify Reset Password Token API View"""
    permission_classes = (AllowAny,)
    serializer_class = VerifyResetPasswordSerializer

    def post(self, *args, **kwargs):
        payload = self.request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            user = get_user_model().objects.filter(email=payload.get('email'))
            if user.exists():
                user = user.first()
                if user.is_active:
                    token = payload.get('token')
                    if ResetPasswordTokenHelper.validate_token(user=user, token=token):
                        user.set_password(payload.get('new_password'))
                        response = {
                            'message': 'Password updated successfully.'
                        }
                        code = status.HTTP_202_ACCEPTED
                    else:
                        response = {
                            'message': 'Token is invalid.'
                        }
                        code = status.HTTP_404_NOT_FOUND
                else:
                    response = {
                        'message': 'Account is not active.'
                    }
                    code = status.HTTP_403_FORBIDDEN
            else:
                response = {
                    'message': 'User not found.'
                }
                code = status.HTTP_404_NOT_FOUND
        else:
            response = serializer.errors
            code = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=code
        )
