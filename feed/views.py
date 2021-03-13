from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from actstream.actions import follow, unfollow
from rest_framework.permissions import IsAuthenticated

from user.models import User


class FollowUserAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, username: str):
        user = request.user
        if username.lower() == user.username.lower():
            return Response(
                {'error': "Can't follow yourself."}, status=status.HTTP_400_BAD_REQUEST
            )
        to_follow = get_object_or_404(User, username__iexact=username)
        follow(request.user, to_follow)
        return Response({'followed': True})


class UnfollowUserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, username: str):
        to_unfollow = get_object_or_404(User, username__iexact=username)
        unfollow(request.user, to_unfollow)
        return Response({'unfollowed': True})
