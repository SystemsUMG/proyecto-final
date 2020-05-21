from django.shortcuts import render
from  django.http import HttpResponse
from TiendaEquipo.forms import FormularioCliente, FormularioPrueba
from TiendaEquipo.models import Cliente
from django.shortcuts import redirect

# Create your views here.

def nuevo_cliente(request):
    if request.method == "POST":
        form = FormularioCliente(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("lista_clientes")

    else:
        form = FormularioCliente()      

    return render(request, "TiendaEquipo/nuevo_cliente.html", {'form': form})

def home(request):

    return render(request, "TiendaEquipo/home.html")

def prueba(request):
    if request.method == "POST":
        form = FormularioPrueba(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = FormularioPrueba()  

    return render(request, "TiendaEquipo/prueba.html", {'form': form})

def lista_clientes(request):

    return render(request, "TiendaEquipo/lista_clientes.html")