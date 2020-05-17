from django import forms
from TiendaEquipo.models import Cliente

class FormularioCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'