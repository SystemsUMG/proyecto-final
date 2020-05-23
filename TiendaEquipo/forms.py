from django import forms
from TiendaEquipo.models import Cliente, Prueba, Proveedor, Producto, Venta
from django.forms import ModelForm
import datetime

fecha_actual = datetime.date.today() - datetime.timedelta(days=1)
fecha_futura = datetime.date.today() + datetime.timedelta(days=2190)

class FormularioCliente(ModelForm):
        
    dpi = forms.CharField(
        min_length=13, 
        max_length=13,
        label='DPI',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    nombre = forms.CharField(
        min_length=2, 
        max_length=35,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    apellido = forms.CharField(
        min_length=2,
        max_length=35,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    direccion = forms.CharField(
        min_length=3,
        max_length=50,
        label='Dirección',
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
        )
    
    telefono = forms.CharField(
        min_length=8,
        max_length=8,
        label='Teléfono',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    nit = forms.CharField(
        min_length=8,
        max_length=9,
        label='NIT',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    tarjeta = forms.CharField(
        min_length=16,
        max_length=16,
        label='Número de Tarjeta',
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    clave = forms.CharField(
        min_length=3,
        max_length=3,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
    )

    fecha_tarjeta = forms.DateField(
        label='Fecha de Vencimiento',
        widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input', 'type': 'date',
        'min':fecha_actual,
        'max':fecha_futura,
        }),
    )

    class Meta:
        model = Cliente
        fields = '__all__'

class FormularioPrueba(ModelForm):
    prueba1 = forms.IntegerField(
        max_value=999, 
        min_value=000, 
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label = 'Código',
    )

    prueba2 = forms.EmailField( 
        widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Email',
    )

    class Meta:
        model = Prueba
        fields = ['prueba1', 'prueba2', 'prueba3']

class FormularioProveedor(ModelForm):
    nombre = forms.CharField(
        max_length=25,
        min_length=2,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'})
    )

    direccion = forms.CharField(
        max_length=45,
        min_length=4,
        widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Dirección',
    )

    telefono = forms.CharField(
        max_length=8,
        min_length=8,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Teléfono',
    )

    nit = forms.CharField(
        max_length=9,
        min_length=8,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}),
        label='NIT',
    )

    correo = forms.EmailField( 
        widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}),
        label='Email',
    )

    class Meta:
        model = Proveedor
        fields = '__all__'

class FormularioProducto(ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
    
class FormularioVenta(ModelForm):
    numeroVenta = forms.CharField(
       min_length=1,
       max_length=3,
       widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'})
    )

    cantidad = forms.CharField(
        min_length=1,
        max_length=3,
        widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'})
    )

    class Meta:
        model = Venta
        fields = '__all__'