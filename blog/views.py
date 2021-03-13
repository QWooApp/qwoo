from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from blog.models import Post
from user.models import User
from blog.serializers import PostListSerializer, PostCreateSerializer


class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated,)


class DeletePostAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.posts.all()


class RecentPublicPostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        user = self.request.user
        if user.is_authenticated:
            context['heart__post_ids'] = user.hearts.values_list('post_id', flat=True)
        else:
            context['heart__post_ids'] = []

        return context

    def get_queryset(self):
        return Post.objects.all().select_related('user', 'reply_to', 'reply_to__user')[
            :20
        ]
