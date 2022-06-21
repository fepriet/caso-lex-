from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import FormularioAddTramites, NuevoUsuario, FormularioCliente, FormularioModUsuario, FormularioModCliente
from .models import Causa, Cliente, Tramite
from django.db import transaction
#from django.contrib.auth.models import User

# Create your views here.
def home(request):

    return render(request,'home.html')

#Registro de usuario con datos propios del cliente.
def registro(request):
    if request.method == "POST":
        form_usuario = NuevoUsuario(request.POST)
        form_cliente = FormularioCliente(request.POST)
        if form_usuario.is_valid() and form_cliente.is_valid():
            usuario = form_usuario.save()
            usuario.refresh_from_db()
            form_cliente = FormularioCliente(request.POST, instance=usuario.cliente)
            form_cliente.full_clean()
            form_cliente.save()
            return redirect('home')
    else:
        datos = {
            'form_usuario' : NuevoUsuario(),
            'form_cliente' : FormularioCliente()
        }
        return render(request, 'registro.html', datos)

#View que realiza la operacion de login. Solo le interesa el nombre de usuario y la contraseña.
def inicio_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('index')
        else:
            return redirect('index')
    datos = {
        'formulario': AuthenticationForm()
    }
    return render(request, 'login.html', datos)

#Esta es una view intermedia que determina cual es tu nivel de acceso (staff o cliente)
#Y redirige al controlador correcto
#Requiere debuggear y trabajar con el sistema de accesos
def login_redirect(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('controlador_staff')
        else:
            return redirect('panel')
    else:
        return redirect('index')

##View para el panel de control del cliente
#Este muestra los datos y el listado de sus causar
def panel_control(request):
    usuario_actual = request.user.id
    if request.user.cliente.is_abogado:
        causas = Causa.objects.all()
    else:
        causas = Causa.objects.all().filter(clientes__usuario__id=usuario_actual)
    datos = {
        'causas' : causas,
        'usuario': usuario_actual
    }
    
    return render(request, 'panel_cliente.html', datos)

#View para el formulario de modificacion de datos del cliente
@transaction.atomic
def mod_cliente(request):
    if request.method == "POST":
        form_usuario = FormularioModUsuario(request.POST, instance=request.user)
        form_cliente = FormularioModCliente(request.POST, instance=request.user.cliente)
        if form_usuario.is_valid() and form_cliente.is_valid():
            form_usuario.save()
            form_cliente.save()
            return redirect('perfil')
        else:
            return redirect('perfil')
    else:
        datos = {
            'form_usuario' : FormularioModUsuario(instance=request.user),
            'form_cliente' : FormularioModCliente(instance=request.user.cliente)
        }
        return render(request, 'mod_cliente.html', datos)

#View para ver los datos especificos de una causa
#Este requiere la id de la causa en la url
def detalle_causa(request, id):
    causa_actual = Causa.objects.get(id=id)
    tramites = Tramite.objects.all().filter(causa__id=id)
    datos = {
        'causa': causa_actual,
        'tramites': tramites
    }
    return render(request, 'detalle_causa.html', datos)

#View para añadir tramites a una causa
#El ID corresponde al ID de la causa a la cual se añadira el tramite
def add_tramite(request, id):
    if request.method == "POST":
        formulario_tramite = FormularioAddTramites(request.POST)
        if formulario_tramite.is_valid():
            tramite = formulario_tramite.save(commit=False)
            tramite.causa = Causa.objects.get(id=id)
            tramite.save()
            return redirect('home')
        else:
            return redirect('perfil')
    else:
        datos = {
            'form' : FormularioAddTramites
        }
        return render(request, 'add_tramite.html', datos)

#View para eliminar todos los usuarios
#def borrar_clientes(request):
 #   User.objects.all().delete()
  #  Cliente.objects.all().delete()

   # return redirect('home')