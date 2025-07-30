# blog/urls.py

from django.urls import path
from . import views # Importa tus vistas

urlpatterns = [
    # URL para la lista de todas las películas
    path('', views.lista_peliculas, name='lista_peliculas'),

    # URL para el detalle de una película específica (usando su ID)
    # CAMBIO AQUÍ: 'pelicula_id' se cambió a 'pk' para coincidir con la vista
    path('pelicula/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),

    # URL para la pantalla de inicio de sesión/registro
    path('accounts/login_register/', views.inicio_sesion_registro, name='inicio_sesion_registro'),

    # URL para cerrar sesión
    path('accounts/logout/', views.cerrar_sesion, name='cerrar_sesion'),
]