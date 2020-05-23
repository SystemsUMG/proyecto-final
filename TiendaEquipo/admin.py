from django.contrib import admin
from TiendaEquipo.models import Cliente, Prueba, Proveedor, Producto, Venta

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "dpi", "telefono")
    search_fields= ("nombre", "apellido", "dpi")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Prueba)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)