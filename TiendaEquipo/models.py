from django.db import models

# Create your models here.

class Cliente(models.Model):
    email = models.EmailField(verbose_name="Correo Electrónico")
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    telefono = models.CharField(max_length=8, verbose_name="Teléfono")
    dpi = models.CharField(max_length=13, verbose_name="DPI")
    nit = models.CharField(max_length=9, verbose_name="NIT")
    tarjeta = models.CharField(max_length=16)
    clave = models.CharField(max_length=3, verbose_name="Clave")
    fecha_tarjeta = models.DateField(verbose_name="Vencimiento")
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return "%s %s" %(self.apellido, self.nombre)