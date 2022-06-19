from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

#Formularios de creacion de usuarios
#Primero se utilizara el formulario de creacion de usuario

class NuevoUsuario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NuevoUsuario, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

#Este formulario procesa los datos de usuario en caso de necesitar actualizarlos
class FormularioUsuario(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email',)

#Formulario que procesa los datos del modelo Cliente
class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('p_nombre', 's_nombre', 'ap_paterno', 'ap_materno', 'direccion')