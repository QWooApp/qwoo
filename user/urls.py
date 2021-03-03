from django.urls import path

from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView,
)

app_name = 'user'

urlpatterns = [
    # Token based views
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
]
