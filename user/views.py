from django.conf import settings

from rest_framework import status
from google.oauth2 import id_token
from rest_framework.views import APIView
from google.auth.transport import requests
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.serializers import UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class GoogleUserRegisterAPIView(APIView):
    """ Creates user via Google's OAuth 2.0 """

    @staticmethod
    def post(request: Request) -> Response:
        token = request.POST.get('token')
        if not token:
            return Response(
                {'error': 'Token not provided.'}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), settings.GOOGLE_OAUTH2_KEY
            )
            if idinfo['iss'] not in (
                'accounts.google.com',
                'https://accounts.google.com',
            ):
                raise Exception('Wrong issuer.')
            email = idinfo.pop('email')
            first_name, last_name = idinfo.pop('given_name'), idinfo.pop(
                'family_name', ''
            )
            username = f'{first_name}-{User.objects.values("id").count()}'.lower()
            created = False
            try:
                user = User.objects.get(email__iexact=email)
            except User.DoesNotExist:
                user, created = User.objects.get_or_create(
                    email=email,
                    is_active=True,
                    username=username,
                    last_name=last_name,
                    first_name=first_name,
                )
            return Response(
                {
                    'username': user.username,
                    'token': str(RefreshToken.for_user(user).access_token),
                },
                status=(status.HTTP_201_CREATED if created else status.HTTP_200_OK),
            )
        except ValueError:
            return Response(
                {'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST
            )
