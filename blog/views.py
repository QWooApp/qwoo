from django.core.cache import cache

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView

from blog.models import Post
from user.models import User
from blog.serializers import PostListSerializer, PostCreateSerializer


class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated,)


class RecentPublicPostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        qs = cache.get('recent_public_posts')
        if qs:
            return qs
        else:
            qs = Post.objects.filter(user__privacy=User.PUBLIC)[:20]
            cache.set('recent_public_posts', qs)
            return qs
