from django.shortcuts import get_object_or_404

from actstream.models import Action
from rest_framework import serializers

from user.models import User
from user.serializers import UserListSerializer
from notifications.models import STARTED_FOLLOWING


# noinspection PyMethodMayBeStatic
class NotificationSerializer(serializers.ModelSerializer):

    actor_object = serializers.SerializerMethodField()
    target_object = serializers.SerializerMethodField()

    def get_actor_object(self, obj: Action):
        data = UserListSerializer(get_object_or_404(User, pk=obj.actor_object_id)).data
        data['type'] = 'user'
        return data

    def get_target_object(self, obj: Action):
        if obj.verb == STARTED_FOLLOWING:
            data = UserListSerializer(
                get_object_or_404(User, pk=obj.target_object_id)
            ).data
            data['type'] = 'user'
        else:
            data = obj.target_object_id
        return data

    class Meta:
        model = Action
        exclude = (
            'public',
            'actor_object_id',
            'target_object_id',
            'actor_content_type',
            'target_content_type',
            'action_object_content_type',
        )
