from django.urls import path

from heart.views import HeartCreateAPIView, HeartDeleteAPIView

app_name = 'heart'

urlpatterns = [
    path('create/', HeartCreateAPIView.as_view(), name='create'),
    path('delete/<slug:post_id>/', HeartDeleteAPIView.as_view(), name='create'),
]
