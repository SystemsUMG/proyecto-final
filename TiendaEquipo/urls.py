from django.urls import path
from TiendaEquipo.views import cliente, stock

urlpatterns = [
    path('cliente/', cliente, name = ('Cliente')),
    path('stock/', stock, name="Stock")
]