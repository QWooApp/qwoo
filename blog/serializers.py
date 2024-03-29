from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from blog.models import Post
from user.serializers import UserListSerializer


class GetIsHeartedSerializer(serializers.ModelSerializer):

    is_hearted = serializers.SerializerMethodField()

    def get_is_hearted(self, obj: Post):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.id in self.context['heart__post_ids']
        else:
            return False

    class Meta:
        model = Post


class BasePostSerializer(serializers.ModelSerializer):

    user = UserListSerializer(read_only=True)
    reply_count = serializers.IntegerField(read_only=True)
    heart_count = serializers.IntegerField(read_only=True)
    timestamp = serializers.DateTimeField(format='%b %d, %Y', read_only=True)

    class Meta:
        model = Post
        exclude = ('reply_to',)


class SubPostRelatedSerializer(GetIsHeartedSerializer, BasePostSerializer):
    class Meta:
        model = Post
        exclude = ('reply_to',)


class PostListSerializer(GetIsHeartedSerializer, BasePostSerializer):

    reply_to = SubPostRelatedSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(BasePostSerializer):

    reply_to = BasePostSerializer(read_only=True)

    reply_to_id = serializers.UUIDField(
        allow_null=True, write_only=True, required=False
    )

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


class PostDetailSerializer(TaggitSerializer, BasePostSerializer):

    reply_of = SubPostRelatedSerializer()
    hashtags = TagListSerializerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
