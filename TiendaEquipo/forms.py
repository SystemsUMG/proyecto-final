from django import forms
from TiendaEquipo.models import Cliente
from django.forms import ModelForm

import datetime

class FormularioCliente(ModelForm):
        
    dpi = forms.CharField(min_length=13, max_length=13)
    nombre = forms.CharField(min_length=2, max_length=30)
    apellido = forms.CharField(min_length=2, max_length=30)
    direccion = forms.CharField(min_length=3, max_length=50)
    telefono = forms.CharField(min_length=8, max_length=8)
    email = forms.EmailField()
    nit = forms.CharField(min_length=9, max_length=9)
    tarjeta = forms.CharField(min_length=16, max_length=16)
    clave = forms.CharField(min_length=3, max_length=3)

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'fecha_tarjeta': forms.SelectDateWidget(years=range(2020, 2026))
        }

    def clean_fecha_tarjeta(self):
        fecha = self.cleaned_data['fecha_tarjeta']

        if fecha <= datetime.date.today():
            raise forms.ValidationError("La Fecha no Puede ser Menor al Día de Hoy")

        return fecha