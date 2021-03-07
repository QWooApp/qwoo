from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from blog.models import Post
from user.serializers import UserListSerializer


class SubPostListSerializer(serializers.ModelSerializer):

    user = UserListSerializer()
    reply_count = serializers.IntegerField(read_only=True)
    heart_count = serializers.IntegerField(read_only=True)
    repost_count = serializers.IntegerField(read_only=True)
    timestamp = serializers.DateTimeField(format='%b %d, %Y', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):

    user = UserListSerializer()
    repost_of = SubPostListSerializer()
    is_hearted = serializers.SerializerMethodField()
    reply_count = serializers.IntegerField(read_only=True)
    heart_count = serializers.IntegerField(read_only=True)
    repost_count = serializers.IntegerField(read_only=True)
    timestamp = serializers.DateTimeField(format='%b %d, %Y', read_only=True)

    def get_is_hearted(self, obj: Post):
        user = self.context['request'].user
        return user.hearts.filter(post_id=obj.id).exists()

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):

    user = UserListSerializer(read_only=True)

    reply_to = serializers.UUIDField(read_only=True)
    repost_of = SubPostListSerializer(read_only=True)

    reply_to_id = serializers.UUIDField(
        allow_null=True, write_only=True, required=False
    )
    repost_of_id = serializers.UUIDField(
        allow_null=True, write_only=True, required=False
    )

    reply_count = serializers.IntegerField(read_only=True)
    heart_count = serializers.IntegerField(read_only=True)
    repost_count = serializers.IntegerField(read_only=True)

    timestamp = serializers.DateTimeField(format='%b %d, %Y', read_only=True)
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
        fields = '__all__'


class PostDetailSerializer(TaggitSerializer, serializers.ModelSerializer):

    user = UserListSerializer()
    hashtags = TagListSerializerField(read_only=True)
    reply_count = serializers.IntegerField(read_only=True)
    heart_count = serializers.IntegerField(read_only=True)
    repost_count = serializers.IntegerField(read_only=True)
    timestamp = serializers.DateTimeField(format='%b %d, %Y', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
