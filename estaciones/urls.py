from django.urls import path
from . import views

app_name = 'estaciones'

urlpatterns = [
    # estaciones
    path('', views.lista_estaciones, name='lista_estaciones'),
    path('crear/', views.crear_estacion, name='crear_estacion'),
    path('<uuid:pk>/editar/', views.editar_estacion, name='editar_estacion'),
    path('<uuid:pk>/eliminar/', views.eliminar_estacion, name='eliminar_estacion'),

    # incidencias
    path('incidencias/', views.lista_incidencias, name='lista_incidencias'),
    path('incidencias/crear/', views.crear_incidencia, name='crear_incidencia'),
    path('incidencias/<uuid:pk>/editar/', views.editar_incidencia, name='editar_incidencia'),
    path('incidencias/<uuid:pk>/eliminar/', views.eliminar_incidencia, name='eliminar_incidencia'),
]
