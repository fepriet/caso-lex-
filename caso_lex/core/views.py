from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import FormularioAddTramites, FormularioCausa, FormularioContrato, NuevoUsuario, FormularioCliente, FormularioModUsuario, FormularioModCliente, FormularioSolicitud
from .models import Causa, Cliente, SolicitudServicio, Tramite, Contrato
from django.db import transaction
from django.contrib.auth.models import User

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
                return redirect('login_redirect')
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
        return redirect('panel')
    else:
        return redirect('index')

##View para el panel de control del cliente
#Este muestra los datos y el listado de sus causar
def panel_control(request):
    usuario_actual = request.user.id
    if request.user.cliente.is_abogado:
        causas = Causa.objects.all()
        datos = {
        'causas' : causas,
        'usuario': usuario_actual
    }
    else:
        causas = Causa.objects.all().filter(clientes__usuario__id=usuario_actual)
        solicitudes = SolicitudServicio.objects.all().filter(solicitante__id=usuario_actual)
        datos = {
            'causas' : causas,
            'usuario': usuario_actual,
            'solicitudes' : solicitudes
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
            'form' : FormularioAddTramites()
        }
        return render(request, 'add_tramite.html', datos)

##Cierre de sesion del usuario
def cierre_sesion(request):
    logout(request)
    return redirect('home')

#View para el formulario de ingreso de solicitudes
@transaction.atomic
def add_solicitud(request):
    if request.method == "POST":
        formulario_solicitud = FormularioSolicitud(request.POST)
        if formulario_solicitud.is_valid():
            solicitud = formulario_solicitud.save(commit=False)
            solicitud.solicitante = request.user
            solicitud.save()
            return redirect('panel')
        else:
            return redirect('home')
    else:
        datos = {
            'formulario' : FormularioSolicitud()
        }
        return render(request, 'add_solicitud.html', datos)

#Eliminar solicitudes
def del_solicitud(request, id):
    solicitud = SolicitudServicio.objects.get(id=id)
    solicitud.delete()
    return redirect('panel')

#Añadir causas
#El acceso debe ser limitado solo a abogados
def add_causa(request):
    if request.method == "POST":
        formulario = FormularioCausa(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('panel')
        else:
            return redirect('home')
    else:
        datos = {
            'formulario' : FormularioCausa()
        }
        return render(request, 'add_causa.html', datos)

#Añadir contratos
#Esto deberia de estar limitado solo al tecnico juridoc
def add_contrato(request):
    if request.method == "POST":
        formulario = FormularioContrato(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('panel_tecnico')
        else:
            return redirect('home')
    else:
        datos = {
            'formulario' : FormularioContrato()
        }
        return render(request, 'add_contrato.html', datos)

def del_contrato(request, id):
    contrato = Contrato.objects.get(id=id)
    contrato.delete()
    return render('panel_tecnico')

def mod_contrato(request, id):
    contrato = Contrato.objects.get(id=id)
    datos = {
        'formulario' : FormularioContrato(instance=contrato) 
    }
    if request.method == "POST":
        formulario = FormularioContrato(instance=contrato)
        if formulario.is_valid():
            formulario.save()
            return redirect('panel_tecnico')
    else:
        return render(request, 'mod_contrato.html', datos)

#Panel de control del tecnico juridico
def panel_tecnico(request):
    solicitudes = SolicitudServicio.objects.all()
    contratos = Contrato.objects.all()
    datos = {
        'solicitudes' : solicitudes,
        'contratos' : contratos
    }

    return render(request, 'panel_tecnico.html', datos)

#View para eliminar todos los usuarios
#def borrar_clientes(request):
 #   User.objects.all().delete()
  #  Cliente.objects.all().delete()

   # return redirect('home')