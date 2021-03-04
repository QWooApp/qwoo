from rest_framework import serializers

from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'username', 'first_name')


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
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'privacy',
            'avatar',
            'bio',
        )
