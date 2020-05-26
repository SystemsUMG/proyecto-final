from django.urls import path
from TiendaEquipo.views import home, redireccion, prueba, nuevo_cliente, lista_clientes, busqueda_clientes, modificar_cliente, eliminar_cliente, proveedores, eliminar_proveedor, nuevo_producto, inventario, modificar_producto, eliminar_producto, ventas, eliminar_venta

urlpatterns = [
    path('home/', home, name='home'),
    path('', redireccion, name='redirect'),
    path('prueba/', prueba, name='prueba'),
    path('nuevo-cliente/', nuevo_cliente, name ='nuevo_cliente'),
    path('lista-clientes/', lista_clientes, name='lista_clientes'),
    path('busqueda-clientes/', busqueda_clientes, name="busqueda_clientes"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name='eliminar_cliente'),
    path('proveedores/', proveedores, name="proveedores"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name='eliminar_proveedor'),
    path('nuevo-producto/', nuevo_producto, name="nuevo_producto"),
    path('inventario/', inventario, name="inventario"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('ventas/', ventas, name="ventas"),
    path('eliminar-venta/<id>/', eliminar_venta, name='eliminar_venta'),
]