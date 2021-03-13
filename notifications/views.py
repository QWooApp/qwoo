from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from actstream.actions import follow

from notifications.serializers import NotificationSerializer


class NotificationListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return user.target_actions.all()
