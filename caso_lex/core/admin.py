from django.contrib import admin
from .models import Abogado, Causa, Cliente, Contrato, Corte, Region, Nacionalidad, EstadoCivil, Comuna, TecnicoJuridico, Tribunal


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Nacionalidad)
admin.site.register(EstadoCivil)
admin.site.register(Abogado)
admin.site.register(Corte)
admin.site.register(Tribunal)
admin.site.register(Causa)
admin.site.register(Contrato)
admin.site.register(TecnicoJuridico)