from django.shortcuts import render
from  django.http import HttpResponse
from TiendaEquipo.forms import FormularioCliente
from TiendaEquipo.models import Cliente
from django.shortcuts import redirect

# Create your views here.

def cliente(request):

    if request.method == "POST":
        
        formulario = FormularioCliente(request.POST, request.FILES)

        if formulario.is_valid():

            formulario.save()        

            return render(request, "TiendaEquipo/stock.html")

    else:

        formulario = FormularioCliente()

    return render(request, "TiendaEquipo/formulario_cliente.html", {"form": formulario})

def stock(request):

    return render(request, "TiendaEquipo/stock.html")