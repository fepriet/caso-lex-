from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Nacionalidad(models.Model):
    descripcion = models.CharField(max_length=30,verbose_name="Nombre de la Nacionalidad")

    def __str__(self):
        return self.descripcion

class EstadoCivil(models.Model):
    descripcion = models.CharField(max_length=15,verbose_name="Estado Civil")

    def __str__(self):
        return self.descripcion

class Region(models.Model):
    nombre= models.CharField(max_length=15,verbose_name="Nombre de la Region")
    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre= models.CharField(max_length=15,verbose_name="Nombre de la Comuna")
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=13,verbose_name="Rut", unique=True)
    p_nombre = models.CharField(max_length=15,verbose_name="Primer Nombre")
    s_nombre =models.CharField(max_length=15,verbose_name="Segundo Nombre")
    ap_paterno=models.CharField(max_length=20,verbose_name="Apellido Paterno")
    ap_materno=models.CharField(max_length=20,verbose_name="Apellido Materno")
    direccion=models.CharField(max_length=50,verbose_name="Direccion")
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)
    id_estado_civil = models.ForeignKey(EstadoCivil,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Cliente.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.cliente.save()


class Estadocontrato(models.Model):
    descripcion = models.CharField(max_length=15,verbose_name="Estado Contrato")
    
    def __str__(self):
        return self.descripcion

class TecnicoJuridico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=13, verbose_name="Rut", unique=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Tecnico Juridico")

    def __str__(self):
        return self.rut

class Abogado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=13, verbose_name="Rut", unique=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Tecnico Juridico")

    def __str__(self):
        return self.rut

class Contrato(models.Model):
    #Un valor de null quiere decir que el contrato es pro bono, se paga por resultado o caulquier otro caso especial
    valor = models.IntegerField(verbose_name="Valor total del contato", null=True)
    archivo_contrato = models.FileField(verbose_name="Archivo del contrato")
    tecnico_juridico = models.ForeignKey(TecnicoJuridico, on_delete=models.CASCADE, verbose_name="Tecnico a cargo del contrato")

class Cuotas(models.Model):
    valor = models.IntegerField(verbose_name="Valor de la cuota")
    #null quiere decir que la cuota no se ha pagado aun
    fecha_pago = models.DateField(verbose_name="Fecha de Pago de la Cuota", null=True)
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento de la cuota")
    contrato = models.ManyToManyField(Contrato, through='DetalleCuotas')

class DetalleCuotas(models.Model):
    cuota = models.ForeignKey(Cuotas, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    pagado = models.BooleanField(verbose_name="Se encuentra o no pagada la cuota")

class Corte(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la corte")

    def __str__(self):
        return self.nombre

class Tribunal(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del tribunal")
    corte = models.ForeignKey(Corte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Causa(models.Model):
    caratulado = models.CharField(max_length=200, verbose_name="Caratulado de la causa")
    rol = models.CharField(max_length=100, verbose_name="Rol de la causa")
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=100, verbose_name="Estado de la causa")
    abogados = models.ManyToManyField(Abogado)
    tribunal = models.ForeignKey(Tribunal, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    clientes = models.ManyToManyField(Cliente)

    def __str__(self):
        return self.caratulado

class Tramite(models.Model):
    folio = models.IntegerField(verbose_name="Folio del presente tramite")
    foja = models.IntegerField(verbose_name="Foja en el archivador")
    documento = models.FileField(verbose_name="Copia del archivo encontrado en la pagina del poder judicial", blank=True)
    etapa = models.CharField(max_length=200, verbose_name="Etapa en la que fue introducido")
    descripcion_tramite = models.TextField()
    fecha_tramite = models.DateField(verbose_name="Fecha del tramite")
    causa = models.ForeignKey(Causa, on_delete=models.CASCADE)