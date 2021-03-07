from django.urls import path

from heart.views import HeartCreateAPIView

app_name = 'heart'

urlpatterns = [
    path('post-heart/', HeartCreateAPIView.as_view(), name='post-heart-create'),
]
