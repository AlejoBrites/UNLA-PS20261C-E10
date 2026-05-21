from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.users.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('games/', include('apps.games.urls')),
    path('cart/', include('apps.cart.urls')),
    path('payments/', include('apps.payments.urls')),
    path('library/', include('apps.library.urls')),
    path('', landing, name='home'),
]

# Servir archivos de medios solo en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
