from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/flota/buses/', permanent=False), name='home'),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('rutas/', include('rutas.urls', namespace='rutas')),
    path('mantenimiento/', include('mantenimiento.urls', namespace='mantenimiento')),
    path('flota/', include('flota.urls', namespace='flota')),
    path('estaciones/', include('estaciones.urls', namespace='estaciones')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Transmi_Admin.views.error_404'
handler500 = 'Transmi_Admin.views.error_500'

