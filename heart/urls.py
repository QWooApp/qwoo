from django.urls import path

from heart.views import HeartCreateAPIView, HeartDeleteAPIView, PostHeartUserListAPIView

app_name = 'heart'

urlpatterns = [
    path('create/', HeartCreateAPIView.as_view(), name='create'),
    path('delete/<uuid:post_id>/', HeartDeleteAPIView.as_view(), name='create'),
    path(
        'hearters/<uuid:post_id>/', PostHeartUserListAPIView.as_view(), name='hearters'
    ),
]
