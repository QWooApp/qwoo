from rest_framework import serializers
from actstream.models import following

from user.models import User


class UserListSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ('avatar', 'username', 'name')


class UserDetailSerializer(serializers.ModelSerializer):

    avatar = serializers.URLField(source='avatar_url')
    is_following = serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(format='%B %Y')

    def get_is_following(self, obj: User) -> bool:
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        else:
            return obj in following(user)

    class Meta:
        model = User
        fields = (
            'bio',
            'avatar',
            'username',
            'last_name',
            'first_name',
            'date_joined',
            'is_following',
            'follow_requested',
        )


class UserUniqueFieldSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    value = serializers.CharField(write_only=True)
    available = serializers.CharField(read_only=True)
    field = serializers.CharField(write_only=True, required=False, default='username')

    def validate(self, attrs):
        field = attrs.get('field')

        if field not in ('username', 'email'):
            raise serializers.ValidationError('Invalid field provided.', code='invalid')

        q_filter = {f'{field}__iexact': attrs.get('value')}

        if User.objects.values('id').filter(**q_filter).exists():
            attrs['available'] = False
        else:
            attrs['available'] = True

        return attrs


class UserCreateSerializer(serializers.ModelSerializer):

    avatar = serializers.ImageField(allow_null=True)
    last_name = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    name = serializers.CharField(write_only=True, required=True)
    bio = serializers.CharField(
        required=False,
        max_length=250,
        style={'base_template': 'textarea.html'},
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'},
    )

    def create(self, validated_data):
        name = validated_data.pop('name')
        password = validated_data.pop('password')
        user = User(**validated_data, is_active=False)
        user.set_full_name(name)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'username',
            'password',
            'privacy',
            'avatar',
            'bio',
            'first_name',
            'last_name',
        )
