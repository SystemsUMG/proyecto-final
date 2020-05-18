from django.urls import path
from TiendaEquipo.views import cliente, home

urlpatterns = [
    path('cliente/', cliente, name ='cliente'),
    path('', home, name='home'),
]