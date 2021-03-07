from django.urls import path

from blog.views import CreatePostAPIView, DeletePostAPIView, RecentPublicPostListAPIView

app_name = 'blog'

urlpatterns = [
    path('create/', CreatePostAPIView.as_view(), name='create'),
    path('recent/', RecentPublicPostListAPIView.as_view(), name='recent'),
    path('delete/<uuid:pk>/', DeletePostAPIView.as_view(), name='delete'),
]
