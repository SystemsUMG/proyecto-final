from django.contrib import admin
from TiendaEquipo.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "dpi", "telefono")
    search_fields= ("nombre", "apellido", "dpi")

admin.site.register(Cliente, ClienteAdmin)