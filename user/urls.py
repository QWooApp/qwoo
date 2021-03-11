from django.urls import path

from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView,
)

from user.views import (
    UserCreateAPIView,
    UserDetailAPIView,
    UserPostListAPIView,
    GoogleUserRegisterAPIView,
    UserUniqueFieldAvailableAPIView,
)

app_name = 'user'

urlpatterns = [
    # Token based views
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    # Register views
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('google/', GoogleUserRegisterAPIView.as_view(), name='google'),
    path(
        'field-available/',
        UserUniqueFieldAvailableAPIView.as_view(),
        name='field-available',
    ),
    # Retrieve views
    path('posts/<slug:username>/', UserPostListAPIView.as_view(), name='posts'),
    path('detail/<slug:username>/', UserDetailAPIView.as_view(), name='detail'),
]
