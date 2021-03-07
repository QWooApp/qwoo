from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('heart/', include('heart.urls')),
]

if settings.DEBUG:
    urlpatterns.append(
        path('rest/', include('rest_framework.urls')),
    )
