from django.urls import path
from . import views

urlpatterns = [
    path('listar_destinos', views.listar_destinos, name='listar_destinos'),
    path('agregar_destino/', views.agregar_destino, name='agregar_destino'),
    path('modificar_destino/<int:id>', views.modificar_destino, name='modificar_destino'),
    path('eliminar_destino/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
]
