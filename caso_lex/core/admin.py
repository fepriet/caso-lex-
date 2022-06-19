from django.contrib import admin
from .models import Cliente, Region, Nacionalidad, EstadoCivil, Comuna


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Nacionalidad)
admin.site.register(EstadoCivil)