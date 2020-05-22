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
    clientes = Cliente.objects.all()

    return render(request, "TiendaEquipo/lista_clientes.html", {'clientes': clientes})

def busqueda_clientes(request):
    if request.GET["cli"]:
        cliente = request.GET["cli"]

        if len(cliente) > 30:
            mensaje = "Nombre Demasiado Largo"

        else:
            clientes = Cliente.objects.filter(nombre__icontains = cliente)
            return render(request, "TiendaEquipo/resultado_clientes.html", {"clientes": clientes, "query": cliente})
    
    else:
        mensaje = "Por Favor Ingrese Datos al Realizar la Búsqueda"

    return render(request, "TiendaEquipo/resultado_clientes.html", {"mensaje": mensaje})

def modificar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    data = {
        'form': FormularioCliente(instance=cliente)
    }
    if request.method == "POST":
        formulario = FormularioCliente(data=request.POST, instance=cliente, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Modificado Correctamente'
        data['form'] = FormularioCliente(instance=Cliente.objects.get(id=id))

    return render(request, 'TiendaEquipo/modificar_cliente.html', data)