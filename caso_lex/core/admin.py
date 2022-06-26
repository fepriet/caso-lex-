from django.contrib import admin
from .models import Abogado, Causa, Cliente, Contrato, Corte, EstadoPresupuesto, Region, Nacionalidad, EstadoCivil, Comuna, SolicitudServicio, TecnicoJuridico, Tramite, Tribunal


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
admin.site.register(Tramite)
admin.site.register(SolicitudServicio)
admin.site.register(EstadoPresupuesto)