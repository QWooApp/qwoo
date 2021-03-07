from rest_framework import serializers

from heart.models import Heart


class HeartSerializer(serializers.ModelSerializer):

    post_id = serializers.UUIDField(write_only=True)

    def create(self, validated_data) -> Heart:
        heart = Heart(**validated_data)
        heart.user = self.context['request'].user
        heart.save()
        return heart

    class Meta:
        model = Heart
        exclude = ('user', 'post')
