from django.urls import path

from blog.views import CreatePostAPIView, RecentPublicPostListAPIView

app_name = 'blog'

urlpatterns = [
    path('create/', CreatePostAPIView.as_view(), name='create'),
    path('recent/', RecentPublicPostListAPIView.as_view(), name='recent'),
]
