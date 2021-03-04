from rest_framework import serializers

from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'username', 'first_name')


class UserCreateSerializer(serializers.ModelSerializer):

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
            'bio',
        )
