from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login', views.inicio_sesion, name='login'),
    path('registro', views.registro, name='registro'),
    path('panel', views.panel_control, name='panel'),
]