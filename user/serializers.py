from rest_framework.serializers import ModelSerializer

from user.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'avatar')
