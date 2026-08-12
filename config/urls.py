from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings

base_url = settings.BASE_URL

from compras.router import urlpatterns_compras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('redoc/', SpectacularRedocView.as_view(url='/schema/'), name='redoc'),
    path('swagger/', SpectacularSwaggerView.as_view(url='/schema/'), name='swagger-ui'),
    path(f'{base_url}/', include(urlpatterns_compras))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)