from django.shortcuts import render
from  django.http import HttpResponse
from TiendaEquipo.forms import FormularioRegistro
from TiendaEquipo.models import Cliente
from django.shortcuts import redirect

# Create your views here.

def registro(request):

    if request.method == "POST":
        
        formulario = FormularioRegistro(request.POST, request.FILES)

        if formulario.is_valid():

            formulario.save()        

            return render(request, "stock.html")

    else:

        formulario = FormularioRegistro()

    return render(request, "formulario_registro.html", {"form": formulario})

def stock(request):

    return render(request, "stock.html")