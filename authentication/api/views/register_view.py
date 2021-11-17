from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.api.serializers.register_serializer import RegisterSerializer


class RegisterAPIView(APIView):
    """Register API View"""
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, *args, **kwargs):
        payload = self.request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            get_user_model().objects.create_user(**payload)
            response = serializer.data
            code = status.HTTP_201_CREATED
        else:
            response = serializer.errors
            code = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=code
        )
