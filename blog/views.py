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
        return Post.objects.filter(user__privacy=User.PUBLIC).select_related('user')[
            :20
        ]
