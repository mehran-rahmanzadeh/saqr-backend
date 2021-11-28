from rest_framework.serializers import ModelSerializer

from customer_club.models import Notification, UserNotification


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'subject',
            'body',
            'image'
        )


class UserNotificationSerializer(ModelSerializer):
    notification = NotificationSerializer()

    class Meta:
        model = UserNotification
        fields = (
            'sku',
            'notification',
        )
