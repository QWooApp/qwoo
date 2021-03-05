from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from qwoo.views import FaviconView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('qwoo.api')),
    path('favicon.ico', FaviconView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
