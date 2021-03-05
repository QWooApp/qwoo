from django.core.cache import cache

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView

from blog.models import Post
from user.models import User
from blog.serializers import PostListSerializer, PostCreateSerializer

CNT = 0


class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated,)


class RecentPublicPostListAPIView(ListAPIView):
    cache_results = None
    serializer_class = PostListSerializer

    def get_queryset(self):
        if self.cache_results:
            return self.cache_results
        qs = cache.get('recent_public_posts')
        if qs:
            self.cache_results = qs
            return qs
        else:
            qs = Post.objects.filter(user__privacy=User.PUBLIC).select_related('user')[
                :20
            ]
            cache.set('recent_public_posts', qs)
            self.cache_results = qs
            return qs
