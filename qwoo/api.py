from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('feed/', include('feed.urls')),
    path('heart/', include('heart.urls')),
    path('notifications/', include('notifications.urls')),
]

if settings.DEBUG:
    urlpatterns.append(
        path('rest/', include('rest_framework.urls')),
    )
