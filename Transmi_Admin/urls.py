from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('rutas/', include('rutas.urls')),
    path('mantenimiento/', include('mantenimiento.urls')),
    path('flota/', include('flota.urls')),
    path('estaciones/', include('estaciones.urls')),
]
