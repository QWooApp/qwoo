from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from blog.models import Post
from user.serializers import UserListSerializer


class PostListSerializer(serializers.ModelSerializer):

    user = UserListSerializer()
    timestamp = serializers.DateTimeField(format='%b %d, %Y')

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):

    user = UserListSerializer(read_only=True)
    body = serializers.CharField(
        required=False,
        max_length=250,
        style={'base_template': 'textarea.html'},
    )

    def create(self, validated_data):
        post = Post(**validated_data)
        post.user = self.context['request'].user
        post.save()
        return post

    class Meta:
        model = Post
        exclude = ('is_reply', 'reply_to')


class PostDetailSerializer(TaggitSerializer, serializers.ModelSerializer):

    user = UserListSerializer()
    hashtags = TagListSerializerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
