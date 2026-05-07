from django.urls import path
from . import views

app_name = 'rutas'

urlpatterns = [
    # rutas
    path('', views.lista_rutas, name='lista_rutas'),
    path('crear/', views.crear_ruta, name='crear_ruta'),
    path('<uuid:pk>/editar/', views.editar_ruta, name='editar_ruta'),
    path('<uuid:pk>/eliminar/', views.eliminar_ruta, name='eliminar_ruta'),

    # portales
    path('portales/', views.lista_portales, name='lista_portales'),
    path('portales/crear/', views.crear_portal, name='crear_portal'),
    path('portales/<uuid:pk>/editar/', views.editar_portal, name='editar_portal'),
    path('portales/<uuid:pk>/eliminar/', views.eliminar_portal, name='eliminar_portal'),
]
