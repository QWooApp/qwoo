from django.urls import path

from notifications.views import NotificationListAPIView

app_name = 'notifications'

urlpatterns = [
    path('list/', NotificationListAPIView.as_view(), name='list'),
]
