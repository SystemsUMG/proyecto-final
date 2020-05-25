from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

CATEGORIES_CHOICES = [
        ('Escritorio', (
            ('nuevas', 'Nuevas'),
            ('semi nuevas', 'Semi Nuevas'),
            ('gaming', 'Gaming'),
            ('todo_uno', 'Todo en uno'),
            ('oficina', 'Oficina'),
          )
        ),  
        ('NoteBook', (
            ('nuevas', 'Nuevas'),
            ('semi nuevas', 'Semi Nuevas'),
            ('gaming', 'Gaming'),
            ('ultrabook', 'UltraBook'),
            ('pulgadas', 'Pulgadas (13",15",16.5")'),
          )
        ),
        ('Componentes', (
            ('teclados', 'Teclados'),
            ('mouse', 'Mouse'),
            ('tarjetas_graficas', 'Tarjetas Graficas'),
            ('tarjetas_ram', 'Tarjetas Ram'),
            ('tarjeta_ethernet', 'Tarjeta Ethernet'),
            ('monitores', 'Monitores'),
            ('kit_de_limpieza_y_mantenimiento', 'Kit de limpieza de mantenimiento'),
            ('case', 'Case'),
            ('procesadores', 'Procesadores'),
            ('motherboard', 'Motherboard'),
            ('ventiladores', 'Ventiladores'),
            ('fuente_de_alimentacion', 'Fuente de alimentacion'),
            ('bocinas', 'Bocinas'),
            ('discos_duro', 'Discos duro'),
            ('disco_estado_solido', 'Disco estado solido'), 
            ('web_cam', 'Web Cam'),
            ('memorias_usb', 'Memorias USB'),
            ('lector_de_cd', 'Lector de sD'),
            ('cd_room', 'CD-ROM'),
            ('impresoras', 'Impresoras'),
            ('bandas_ide_y_sata', 'Bandas IDE y SATA'),
          )
        ),
    ]

PAYMENT_CHOICES = [
    ('tarjeta', 'Tarjeta'),
    ('efectivo', 'Efectivo'),
]

class Cliente(models.Model):
    dpi = models.CharField(max_length=13, verbose_name="DPI", unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    telefono = models.CharField(max_length=8, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")
    nit = models.CharField(max_length=9, verbose_name="NIT")
    tarjeta = models.CharField(max_length=16)
    clave = models.CharField(max_length=3)
    fecha_tarjeta = models.DateField(verbose_name="Vencimiento")
    foto = models.ImageField(null=True, blank=True, upload_to='clientes')

    def __str__(self):
        return '%s %s' %(self.apellido, self.nombre)

class Prueba(models.Model):
    prueba1 = models.IntegerField()
    prueba2 = models.EmailField()
    prueba3 = models.ImageField()

    def __str__(self):
        return '%s' %self.prueba1
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    direccion = models.CharField(max_length=45)
    telefono = models.IntegerField()
    correo = models.EmailField()
    nit = models.CharField(max_length=9)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    categoria = models.CharField(max_length=35, choices=CATEGORIES_CHOICES, default='NoteBook')
    unidades = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    precio_total_compra = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    fecha_ingreso = models.DateField()
    foto_producto = models.ImageField()
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre_producto

class Venta(models.Model):
    numeroVenta= models.IntegerField(verbose_name="No. Venta", unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago= models.CharField(max_length=9, choices=PAYMENT_CHOICES)
    fecha= models.DateField(verbose_name="Fecha")
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return '%s' %self.cliente

def foto_delete(sender, instance, **kwargs):
    instance.foto.delete(False)

post_delete.connect(foto_delete, sender=Cliente)