from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, DestroyAPIView

from heart.models import Heart
from heart.serializers import HeartSerializer


class HeartCreateAPIView(CreateAPIView):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    permission_classes = (IsAuthenticated,)


class HeartDeleteAPIView(DestroyAPIView):
    lookup_field = 'post_id'
    lookup_url_kwarg = 'post_id'
    queryset = Heart.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Heart, user=user, post_id=post_id)
