from django.db import models

# Create your models here.

class Cliente(models.Model):
    dpi = models.CharField(max_length=13, verbose_name="DPI")
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    telefono = models.CharField(max_length=8, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")
    nit = models.CharField(max_length=9, verbose_name="NIT")
    tarjeta = models.CharField(max_length=16)
    clave = models.CharField(max_length=3)
    fecha_tarjeta = models.DateField(verbose_name="Vencimiento")
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '%s %s' %(self.apellido, self.nombre)

class Prueba(models.Model):
    prueba1 = models.IntegerField()
    prueba2 = models.EmailField()
    prueba3 = models.ImageField()

    def __str__(self):
        return '%s' %self.prueba1
    