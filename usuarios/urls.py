from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('<uuid:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('<uuid:pk>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('<uuid:pk>/recargar/', views.recargar_tarjeta, name='recargar_tarjeta'),
]
