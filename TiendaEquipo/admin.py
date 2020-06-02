from django.contrib import admin
from TiendaEquipo.models import Cliente, Proveedor, Producto, Venta

#Registre sus Modelos.

#Mostrar los registros de Cliente en en Panel de Administración.
class ClienteAdmin(admin.ModelAdmin):
    #Campos a mostrar.
    list_display = ("nombre", "apellido", "dpi", "email", "telefono")
    #Campos para realizar búsquedas.
    search_fields= ("nombre", "apellido", "dpi")

#Mostrar los registros de Proveedor en en Panel de Administración.
class ProveedorAdmin(admin.ModelAdmin):
    #Campos a mostrar.
    list_display = ("nombre", "telefono", "correo", "nit")
    #Campos para realizar búsquedas.
    search_fields= ("nombre", "correo")

#Mostrar los registros de Producto en en Panel de Administración.
class ProductoAdmin(admin.ModelAdmin):
    #Campos a mostrar.
    list_display = ("nombre_producto", "marca", "unidades", "precio_compra", "precio_venta")
    #Campos para realizar búsquedas.
    search_fields= ("nombre_producto", "marca", "categoria")
    #Campos para filtrar registros.
    list_filter=("proveedor", "categoria")

#Mostrar los registros de Venta en en Panel de Administración.
class VentaAdmin(admin.ModelAdmin):
    #Campos a mostrar.
    list_display = ("numeroVenta", "producto", "cliente", "fecha")
    #Campos para realizar búsquedas.
    search_fields= ("producto", "cliente", "pago")

#Registro de clases en el Panel de Administración.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)