from django.urls import path

from feed.views import FollowUserAPIView, UnfollowUserAPIView

app_name = 'feed'

urlpatterns = [
    path('follow/<str:username>/', FollowUserAPIView.as_view(), name='follow'),
    path('unfollow/<str:username>/', UnfollowUserAPIView.as_view(), name='follow'),
]
