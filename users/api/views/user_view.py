from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.api.serializers.user_serializer import UserSerializer


class UserViewset(GenericViewSet, ListModelMixin):
    """User Viewset"""
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    @action(detail=False, methods=['patch', 'put'])
    def edit(self, *args, **kwargs):
        """update user profile"""
        user = self.request.user
        payload = self.request.data
        serializer = self.get_serializer(user, data=payload)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Profile updated successfully.'
            }
            code = status.HTTP_202_ACCEPTED
        else:
            response = serializer.errors
            code = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=code
        )
