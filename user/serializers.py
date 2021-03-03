from rest_framework.serializers import ModelSerializer

from user.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'username', 'first_name')
