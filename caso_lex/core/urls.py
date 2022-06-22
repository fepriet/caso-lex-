from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login', views.inicio_sesion, name='login'),
    path('registro', views.registro, name='registro'),
    path('panel', views.panel_control, name='panel'),
    path('perfil', views.mod_cliente, name='perfil'),
    path('causa/<id>', views.detalle_causa, name='causa'),
    path('add_tramite/<id>', views.add_tramite, name='add_tramite'),
    path('login_redirect', views.login_redirect, name='login_redirect'),
    path('logout', views.cierre_sesion, name='logout'),
    path('add_solicitud', views.add_solicitud, name='add_solicitud'),
    path('del_solicitud/<id>', views.del_solicitud, name='del_solicitud'),
    path('add_causa', views.add_causa, name='add_causa'),
    path('add_contrato', views.add_contrato, name='add_contrato'),
    path('panel_tecnico', views.panel_tecnico, name='panel_tecnico'),
    path('del_contrato/<id>', views.del_contrato, name='del_contrato'),
    path('mod_contrato/<id>', views.mod_contrato, name='mod_contrato'),
]