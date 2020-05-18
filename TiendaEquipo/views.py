from django.shortcuts import render
from  django.http import HttpResponse
from TiendaEquipo.forms import FormularioCliente
from TiendaEquipo.models import Cliente
from django.shortcuts import redirect

# Create your views here.

def cliente(request):
    data = {
        'form': FormularioCliente()
    }

    if request.method == "POST":
        formulario = FormularioCliente(request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Cliente Añadido' 

        data['form'] = formulario      

    return render(request, "TiendaEquipo/formulario_cliente.html", data)

def stock(request):

    return render(request, "TiendaEquipo/stock.html")