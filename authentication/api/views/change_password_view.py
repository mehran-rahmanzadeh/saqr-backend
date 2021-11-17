from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.api.serializers.change_password_serializer import ChangePasswordSerializer


class ChangePasswordAPIView(APIView):
    """Change Password API View"""
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def post(self, *args, **kwargs):
        payload = self.request.data
        user = self.request.user
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            if user.is_active:
                if user.check_password(payload.get('password')):
                    try:
                        validate_password(payload.get('new_password'))
                        user.set_password(payload.get("new_password"))
                        user.save()
                        response = {
                            'message': 'Password updated successfully.'
                        }
                        code = status.HTTP_202_ACCEPTED

                    except ValidationError as e:
                        response = {
                            'message': 'Password is not valid.'
                        }
                        code = status.HTTP_400_BAD_REQUEST
                else:
                    response = {
                        'message': 'Password is incorrect.'
                    }
                    code = status.HTTP_404_NOT_FOUND
            else:
                response = {
                    'message': 'Account is not active.'
                }
                code = status.HTTP_403_FORBIDDEN
        else:
            response = serializer.errors
            code = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=code
        )
