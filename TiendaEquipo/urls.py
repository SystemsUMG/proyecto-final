from django.urls import path
from TiendaEquipo.views import nuevo_cliente, home, prueba, lista_clientes, busqueda_clientes, modificar_cliente, eliminar_cliente, redireccion, proveedores, inventario, nuevo_producto, ventas

urlpatterns = [
    path('nuevo-cliente/', nuevo_cliente, name ='nuevo_cliente'),
    path('home/', home, name='home'),
    path('', redireccion, name='redirect'),
    path('prueba/', prueba, name='prueba'),
    path('lista-clientes/', lista_clientes, name='lista_clientes'),
    path('busqueda-clientes/', busqueda_clientes, name="busqueda_clientes"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name='eliminar_cliente'),
    path('proveedores/', proveedores, name="proveedores"),
    path('inventario/', inventario, name="inventario"),
    path('nuevo-producto/', nuevo_producto, name="nuevo_producto"),
    path('ventas/', ventas, name="ventas"),
]