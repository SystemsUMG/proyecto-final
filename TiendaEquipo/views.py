from django.shortcuts import render, redirect
from  django.http import HttpResponse
from TiendaEquipo.forms import FormularioCliente, FormularioProveedor, FormularioProducto, FormularioVenta
from TiendaEquipo.models import Cliente, Proveedor, Producto, Venta
from django.contrib.auth.decorators import login_required
import datetime

#Creación de Vistas

@login_required
def home(request):
    cantidades = {
        'clientes': Cliente.objects.all(),
        'proveedores': Proveedor.objects.all(),
        'productos': Producto.objects.all(),
        'ventas': Venta.objects.all(),
        'categorias': 38,
    }
    return render(request, "TiendaEquipo/home.html", cantidades)

def redireccion(request):
    return redirect('login')

def nuevo_cliente(request):
    if request.method == "POST":
        form = FormularioCliente(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("lista_clientes")

    else:
        form = FormularioCliente() 

    return render(request, "TiendaEquipo/nuevo_cliente.html", {'form': form})

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
    proveedores = Proveedor.objects.all()
    
    if request.method == "POST":
        form = FormularioProveedor(request.POST)

        if form.is_valid():
            form.save()
            return redirect("proveedores")

    else:
        form = FormularioProveedor()

    return render(request, "TiendaEquipo/proveedores.html", {'form': form, 'proveedores': proveedores})

def modificar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    data = {
        'form': FormularioProveedor(instance=proveedor)
    }

    if request.method == "POST":
        formulario = FormularioProveedor(data=request.POST, instance=proveedor, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect("proveedores")

        data['form'] = FormularioProveedor(instance=Proveedor.objects.get(id=id))

    return render(request, 'TiendaEquipo/modificar_proveedor.html', data)

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()

    return redirect("proveedores")

def nuevo_producto(request):
    if request.method == "POST":
        form = FormularioProducto(request.POST, files=request.FILES)

        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.fecha_ingreso = datetime.date.today()
            nuevas_unidades = form.cleaned_data['unidades']
            precio = form.cleaned_data['precio_compra']
            nuevo_producto = form.cleaned_data['nombre_producto']
            formulario.precio_total_compra = nuevas_unidades * precio
            producto = Producto.objects.filter(nombre_producto=nuevo_producto)

            if producto:
                unidades = producto.unidades
                total_unidades = unidades + nuevas_unidades
                producto.unidades = total_unidades
                producto.save()
                return redirect("inventario")

            else:
                formulario.save()
                return redirect("inventario")

    else:
        form = FormularioProducto()
    
    return render(request, "TiendaEquipo/nuevo_producto.html", {'form': form})

def inventario(request):
    productos = Producto.objects.all()
    
    return render(request, "TiendaEquipo/inventario.html", {'productos': productos})

def productos(request):
    productos = Producto.objects.all()

    return render(request, "TiendaEquipo/productos.html", {'productos': productos})

def anadir_unidades(request, id):
    if request.GET["cant"]:
        get = request.GET["cant"]
        nuevas_unidades = int(get)
        producto = Producto.objects.get(id=id)
        unidades = producto.unidades
        total_unidades = unidades + nuevas_unidades
        producto.unidades = total_unidades
        producto.save()

    else:
        nuevas_unidades = 0
        producto = Producto.objects.get(id=id)
        unidades = producto.unidades
        total_unidades = unidades + nuevas_unidades
        producto.unidades = total_unidades
        producto.save()

    return redirect("productos")

def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form': FormularioProducto(instance=producto)
    }

    if request.method == "POST":
        formulario = FormularioProducto(data=request.POST, instance=producto, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect("inventario")

        data['form'] = FormularioProducto(instance=Producto.objects.get(id=id))

    return render(request, 'TiendaEquipo/modificar_producto.html', data)

def busqueda_productos(request):
    if request.GET["prod"]:
        producto = request.GET["prod"]

        if len(producto) > 50:
            mensaje = "Nombre de Producto Demasiado Largo"

        else:
            productos = Producto.objects.filter(nombre_producto__icontains = producto)
            return render(request, "TiendaEquipo/resultado_productos.html", {"productos": productos, "query": producto})
    
    else:
        mensaje = "Por Favor Ingrese Datos al Realizar la Búsqueda"

    return render(request, "TiendaEquipo/resultado_productos.html", {"mensaje": mensaje})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect("inventario")

def ventas(request):
    mensaje = ''
    ventas = Venta.objects.all()

    if request.method == "POST":
        form = FormularioVenta(request.POST)

        if form.is_valid():
            venta = form.save(commit=False)
            venta.fecha = datetime.date.today()
            cantidad = form.cleaned_data['cantidad']
            nombre = form.cleaned_data['producto']
            producto = Producto.objects.get(nombre_producto=nombre)
            unidades = producto.unidades

            if cantidad > unidades:
                mensaje = f'No existen suficientes unidades, por favor ingrese una cantidad menor o igual a {unidades}'

            else:
                venta.total = cantidad * producto.precio_venta
                venta.save()
                total_unidades = unidades - cantidad
                producto.unidades = total_unidades
                producto.save()
                return redirect("ventas")

    else:
        form = FormularioVenta()

    return render(request, "TiendaEquipo/ventas.html", {'form': form, 'ventas': ventas, 'mensaje': mensaje})

def eliminar_venta(request, id):
    venta = Venta.objects.get(id=id)
    nombre = venta.producto
    producto = Producto.objects.get(nombre_producto=nombre)
    unidades = producto.unidades
    cantidad = venta.cantidad
    nuevas_unidades = unidades + cantidad
    producto.unidades = nuevas_unidades
    producto.save()
    venta.delete()
    return redirect("ventas")

def factura(request, id):
    ventas = Venta.objects.get(id=id)
    producto_busqueda = ventas.producto
    producto = Producto.objects.get(nombre_producto=producto_busqueda)
    precio = producto.precio_venta
    id_busqueda = ventas.cliente.id
    cliente = Cliente.objects.get(id=id_busqueda)
    direccion = cliente.direccion
    nit = cliente.nit
    numero = ventas.numeroVenta
    numero_factura = numero + 1100
    data = {
        'ventas':ventas ,
        'precio': precio,
        'nit': nit,
        'direccion': direccion,
        'numero': numero_factura
    }
    
    return render(request, 'TiendaEquipo/factura.html', data)