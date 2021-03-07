from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from user.models import User
from heart.models import Heart
from heart.serializers import HeartSerializer
from user.serializers import UserListSerializer


class HeartCreateAPIView(CreateAPIView):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    permission_classes = (IsAuthenticated,)


class PostHeartUserListAPIView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return User.objects.filter(hearts__post_id=post_id)


class HeartDeleteAPIView(DestroyAPIView):
    lookup_field = 'post_id'
    lookup_url_kwarg = 'post_id'
    queryset = Heart.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Heart, user=user, post_id=post_id)
