from django.contrib import admin
from TiendaEquipo.models import Cliente, Prueba, Proveedor, Producto, Venta

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dpi", "email", "telefono")
    search_fields= ("nombre", "apellido", "dpi")

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "correo", "nit")
    search_fields= ("nombre", "correo")

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre_producto", "marca", "unidades", "precio_compra", "precio_venta")
    search_fields= ("nombre_producto", "marca", "categoria")
    list_filter=("proveedor", "categoria")

class VentaAdmin(admin.ModelAdmin):
    list_display = ("numeroVenta", "producto", "cliente", "fecha")
    search_fields= ("producto", "cliente", "pago")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Prueba)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)