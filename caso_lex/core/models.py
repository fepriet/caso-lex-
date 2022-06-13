from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Nacionalidad(models.Model):
    id_nac = models.IntegerField(primary_key=True, verbose_name='Id de nacionalidad')
    descripcion = models.CharField(max_length=30,verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.id_nac

class Estado_civil(models.Model):
    id_est = models.IntegerField(primary_key=True, verbose_name='Id de nacionalidad')
    descripcion = models.CharField(max_length=15,verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.id_est
class Region(models.Model):
    id_reg = models.IntegerField(primary_key=True, verbose_name='Id de Comuna')
    nombre= models.CharField(max_length=15,verbose_name="Nombre de la Comuna")
    def __str__(self):
        return self.id_reg
class Comuna(models.Model):
    id_com = models.IntegerField(primary_key=True, verbose_name='Id de Comuna')
    nombre= models.CharField(max_length=15,verbose_name="Nombre de la Comuna")
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_com
class Cliente(models.Model):
    id_cl = models.IntegerField(primary_key=True, verbose_name='Id Cliente')
    rut = models.CharField(max_length=13,verbose_name="Rut")
    p_nombre = models.CharField(max_length=15,verbose_name="Primer Nombre")
    s_nombre =models.CharField(max_length=15,verbose_name="Segundo Nombre")
    ap_paterno=models.CharField(max_length=20,verbose_name="Apellido Paterno")
    ap_materno=models.CharField(max_length=20,verbose_name="Apellido Materno")
    direccion=models.CharField(max_length=50,verbose_name="Direccion")
    password=models.CharField(max_length=20,verbose_name="Contraseña")
    id_comuna_region = models.ForeignKey(Comuna,Region,on_delete=models.CASCADE)
    id_nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)
    id_estado_civil = models.ForeignKey(Estado_civil,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_cl
class Estado_contrato(models.Model):
    id_est_con = IntegerField(primary_key=True, verbose_name="Id Estado Contrato")
    descripcion = models.CharField(max_length=15,verbose_name="Estado Contrato")
    def __str__(self):
        return self.id_est_con
