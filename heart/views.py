from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from heart.models import Heart
from heart.serializers import HeartSerializer


class HeartCreateAPIView(CreateAPIView):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    permission_classes = (IsAuthenticated,)
