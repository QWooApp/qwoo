from rest_framework import serializers

from heart.models import Heart


class HeartSerializer(serializers.ModelSerializer):

    post = serializers.UUIDField()

    class Meta:
        model = Heart
        fields = ('post', 'timestamp')
