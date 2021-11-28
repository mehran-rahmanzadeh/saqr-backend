from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from customer_club.api.serializers.notification_serializer import UserNotificationSerializer
from customer_club.models import UserNotification
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

    @action(detail=False, serializer_class=UserNotificationSerializer, methods=['get'])
    def notifications(self, *args, **kwargs):
        """get users unread notifications"""
        user = self.request.user
        notifications = user.notifications.filter(is_seen=False).select_related('notification')
        serializer = self.get_serializer(notifications, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['post'])
    def read_notification(self, *args, **kwargs):
        payload = self.request.data
        user = self.request.user
        UserNotification.objects.filter(
            sku=payload.get('sku'), user=user).update(is_seen=True)
        return Response(
            data={
                'message': 'Set as read.'
            },
            status=status.HTTP_200_OK
        )
