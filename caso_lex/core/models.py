from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.nombreCategoria