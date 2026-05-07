from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    # ordenes
    path('', views.lista_ordenes, name='lista_ordenes'),
    path('crear/', views.crear_orden, name='crear_orden'),
    path('<uuid:pk>/editar/', views.editar_orden, name='editar_orden'),
    path('<uuid:pk>/eliminar/', views.eliminar_orden, name='eliminar_orden'),

    # repuestos
    path('repuestos/', views.lista_repuestos, name='lista_repuestos'),
    path('repuestos/crear/', views.crear_repuesto, name='crear_repuesto'),
    path('repuestos/<uuid:pk>/editar/', views.editar_repuesto, name='editar_repuesto'),
    path('repuestos/<uuid:pk>/eliminar/', views.eliminar_repuesto, name='eliminar_repuesto'),
]
