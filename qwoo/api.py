from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('rest', include('rest_framework.urls')),
]
