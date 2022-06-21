from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Causa, Cliente, Tramite, SolicitudServicio

#Formularios de creacion de usuarios
#Primero se utilizara el formulario de creacion de usuario

class NuevoUsuario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#Este formulario procesa los datos de usuario en caso de necesitar actualizarlos
class FormularioModUsuario(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email',)

#Formulario que procesa los datos del modelo Cliente
class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('rut', 'p_nombre', 's_nombre', 'ap_paterno', 'ap_materno', 'direccion', 'comuna', 'nacionalidad', 'estado_civil')

class FormularioModCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('p_nombre', 's_nombre', 'ap_paterno', 'ap_materno', 'direccion', 'comuna', 'nacionalidad', 'estado_civil')

class FormularioAddTramites(forms.ModelForm):
    class Meta:
        model = Tramite
        fields = ('folio', 'foja', 'documento', 'etapa', 'descripcion_tramite', 'fecha_tramite')

class FormularioSolicitud(forms.ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = ('resumen_solicitud', 'solicitud')

class FormularioCausa(forms.ModelForm):
    class Meta:
        model = Causa
        fields = ('caratulado', 'rol', 'fecha_ingreso', 'estado', 'abogados', 'tribunal', 'contrato', 'clientes')