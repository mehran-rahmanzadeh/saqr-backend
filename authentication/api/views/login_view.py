from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.api.serializers.login_serializer import LoginSerializer


class LoginAPIView(APIView):
    """Login User API View"""
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, *args, **kwargs):
        payload = self.request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            user = authenticate(
                username=payload.get('username'),
                password=payload.get('password')
            )
            if user:
                if user.is_active:
                    refresh = RefreshToken.for_user(user)
                    response = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                    code = status.HTTP_200_OK
                else:
                    response = {
                        'message': 'Account is not active'
                    }
                    code = status.HTTP_403_FORBIDDEN
            else:
                response = {
                    'message': 'Username or password is incorrect.'
                }
                code = status.HTTP_404_NOT_FOUND
        else:
            response = serializer.errors
            code = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=code
        )
