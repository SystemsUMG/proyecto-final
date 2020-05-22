from django.urls import path
from TiendaEquipo.views import nuevo_cliente, home, prueba, lista_clientes, busqueda_clientes, modificar_cliente, compras

urlpatterns = [
    path('nuevo-cliente/', nuevo_cliente, name ='nuevo_cliente'),
    path('', home, name='home'),
    path('prueba/', prueba, name='prueba'),
    path('lista-clientes/', lista_clientes, name='lista_clientes'),
    path('busqueda-clientes/', busqueda_clientes, name="busqueda_clientes"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('compras/', compras, name="compras"),
]
