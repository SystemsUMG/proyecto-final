from django.urls import path
from TiendaEquipo.views import nuevo_cliente, home, prueba, lista_clientes, busqueda_clientes

urlpatterns = [
    path('nuevo-cliente/', nuevo_cliente, name ='nuevo_cliente'),
    path('', home, name='home'),
    path('prueba/', prueba, name='prueba'),
    path('lista-clientes/', lista_clientes, name='lista_clientes'),
    path('busqueda-clientes/', busqueda_clientes, name="busqueda_clientes"),
]