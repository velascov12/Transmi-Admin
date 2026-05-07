from django.urls import path
from . import views

app_name = 'flota'

urlpatterns = [
    # buses
    path('buses/', views.lista_buses, name='lista_buses'),
    path('buses/crear/', views.crear_bus, name='crear_bus'),
    path('buses/<uuid:pk>/editar/', views.editar_bus, name='editar_bus'),
    path('buses/<uuid:pk>/eliminar/', views.eliminar_bus, name='eliminar_bus'),

    # conductores
    path('conductores/', views.lista_conductores, name='lista_conductores'),
    path('conductores/crear/', views.crear_conductor, name='crear_conductor'),
    path('conductores/<uuid:pk>/editar/', views.editar_conductor, name='editar_conductor'),
    path('conductores/<uuid:pk>/eliminar/', views.eliminar_conductor, name='eliminar_conductor'),
]
