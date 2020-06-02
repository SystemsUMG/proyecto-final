from django import forms
from TiendaEquipo.models import Cliente, Proveedor, Producto, Venta
from django.forms import ModelForm
import datetime

fecha_actual = datetime.date.today() - datetime.timedelta(days=1)
fecha_futura = datetime.date.today() + datetime.timedelta(days=2190)

#Creacion de Formularios

#Formulario utilizado para ingresar datos del cliente y guardarlos en la BBDD.
class FormularioCliente(ModelForm):
    #Se define el campo como tipo caracter.
    dpi = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=13, 
        max_length=13,
        label='DPI',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )
    #Se define el campo como tipo caracter.
    nombre = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=2, 
        max_length=35,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
    )
    #Se define el campo como tipo caracter.
    apellido = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=2,
        max_length=35,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
    )
    #Se define el campo como tipo caracter.
    direccion = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=3,
        max_length=50,
        label='Dirección',
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
        )
    #Se define el campo como tipo caracter.
    telefono = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=8,
        max_length=8,
        label='Teléfono',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )
    #Se define el campo como tipo email.
    email = forms.EmailField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}),
    )
    #Se define el campo como tipo caracter.
    nit = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=8,
        max_length=9,
        label='NIT',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )
    #Se define el campo como tipo caracter.
    tarjeta = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=16,
        max_length=16,
        label='Número de Tarjeta',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )
    #Se define el campo como tipo caracter.
    clave = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_length=3,
        max_length=3,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input', 'type': 'password'}),
    )
    #Se define el campo como tipo fecha.
    fecha_tarjeta = forms.DateField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        label='Fecha de Vencimiento',
        widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input', 'type': 'date',
        'min':fecha_actual,
        'max':fecha_futura,
        }),
    )

    class Meta:
        #Se indica el modelo Cliente al cual hará referencia el formulario y donde se guardarán los datos.
        model = Cliente
        #Se especifica que todos los campos serán mostrados para que el usuario ingrese los datos.
        fields = '__all__'

#Formulario utilizado para ingresar datos del proveedor y guardarlos en la BBDD.
class FormularioProveedor(ModelForm):
    #Se define el campo como tipo caracter.
    nombre = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_length=25,
        min_length=2,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'})
    )
    #Se define el campo como tipo caracter.
    direccion = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_length=45,
        min_length=4,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Dirección',
    )
    #Se define el campo como tipo caracter.
    telefono = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_length=8,
        min_length=8,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Teléfono',
    )
    #Se define el campo como tipo caracter.
    nit = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_length=9,
        min_length=8,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label='NIT',
    )
    #Se define el campo como tipo email.
    correo = forms.EmailField( 
        #Se le asignan atributos que serán interpretados en lenguaje html.
        widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Email',
    )

    class Meta:
        #Se indica el modelo Proveedor al cual hará referencia el formulario y donde se guardarán los datos.
        model = Proveedor
        #Se especifica que todos los campos serán mostrados para que el usuario ingrese los datos.
        fields = '__all__'

#Formulario utilizado para ingresar datos del producto y guardarlos en la BBDD.
class FormularioProducto(ModelForm):
    #Se define el campo como tipo caracter.
    nombre_producto = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_length=50,
        min_length=2,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Producto',
    )
    #Se define el campo como tipo caracter.
    marca = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_length=50,
        min_length=2,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'})
    )
    #Se define el campo como tipo entero.
    unidades = forms.IntegerField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_value=100,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'})
    )
    #Se define el campo como tipo decimal.
    precio_compra = forms.DecimalField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Precio de Compra',
    )
    #Se define el campo como tipo decimal.
    precio_venta = forms.DecimalField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Precio de Venta',
    )
    #Se define el campo como tipo caracter.
    descripcion = forms.CharField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        max_length=500,
        widget=forms.Textarea(attrs={'class' : 'mdl-textfield__input'}),
        label='Descripción',
    )

    class Meta:
        #Se indica el modelo Cliente al cual hará referencia el formulario y donde se guardarán los datos.
        model = Producto
        #Se especifican los campos serán mostrados para que el usuario ingrese los datos, el resto se hará en el archivo views.py
        fields = ['nombre_producto', 'marca', 'unidades', 'precio_compra', 'precio_venta', 'proveedor', 'categoria', 'foto_producto', 'descripcion']

    #Valida la relación entre los precios.
    def clean_precio_venta(self):
        #Obtiene los precios.
        compra = self.cleaned_data['precio_compra']
        venta = self.cleaned_data['precio_venta']
        #Valida que el precio de compra no sea mayor al de venta.
        if compra >= venta:
            raise forms.ValidationError("El precio de venta no puede ser menor o igual al de compra")
        #Retorna el nuevo precio de venta ingresado.
        return venta

#Formulario utilizado para ingresar datos de la venta y guardarlos en la BBDD.
class FormularioVenta(ModelForm):
    #Se define el campo como tipo entero.
    numeroVenta = forms.IntegerField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        min_value=1,
        max_value=999,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Número de Venta'
    )
    #Se define el campo como tipo entero.
    cantidad = forms.IntegerField(
        #Se le asignan atributos que serán interpretados en lenguaje html.
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'})
    )

    class Meta:
        #Se indica el modelo Venta al cual hará referencia el formulario y donde se guardarán los datos.
        model = Venta
        #Se especifican los campos serán mostrados para que el usuario ingrese los datos, el resto se hará en el archivo views.py
        fields = ['numeroVenta', 'cantidad', 'producto', 'cliente', 'pago']