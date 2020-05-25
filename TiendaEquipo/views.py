from django.shortcuts import render, redirect
from  django.http import HttpResponse
from TiendaEquipo.forms import FormularioCliente, FormularioPrueba, FormularioProveedor, FormularioProducto, FormularioVenta
from TiendaEquipo.models import Cliente, Proveedor, Venta, Producto
from django.contrib.auth.decorators import login_required

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

@login_required
def home(request):
    cantidades = {
        'administradores': 5,
        'clientes': Cliente.objects.all(),
        'proveedores': Proveedor.objects.all(),
        'productos': Producto.objects.all(),
        'ventas': Venta.objects.all(),
        'categorias': 38,
    }
    return render(request, "TiendaEquipo/home.html", cantidades)

def redireccion(request):
    return redirect('login')

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
            return redirect("lista_clientes")

        data['form'] = FormularioCliente(instance=Cliente.objects.get(id=id))

    return render(request, 'TiendaEquipo/modificar_cliente.html', data)

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect("lista_clientes")

def proveedores(request):
    if request.method == "POST":
        form = FormularioProveedor(request.POST)

        if form.is_valid():
            form.save()
            return redirect("inventario")

    else:
        form = FormularioProveedor()

    return render(request, "TiendaEquipo/proveedores.html", {'form': form})

def inventario(request):
    productos = Proveedor.objects.all()
    
    return render(request, "TiendaEquipo/inventario.html", {'productos': productos})

def nuevo_producto(request):
    if request.method == "POST":
        form = FormularioProducto(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("inventario")

    else:
        form = FormularioProducto()
    
    return render(request, "TiendaEquipo/nuevo_producto.html", {'form': form})

def ventas(request):
    if request.method == "POST":
        form = FormularioVenta(request.POST)

        if form.is_valid():
            form.save()
            return redirect("inventario")

    else:
        form = FormularioVenta() 

    return render(request, "TiendaEquipo/ventas.html", {'form': form})