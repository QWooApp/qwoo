from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class GoogleUserRegisterAPIView(APIView):
    @staticmethod
    def post(request: Request) -> Response:
        raise NotImplementedError()
