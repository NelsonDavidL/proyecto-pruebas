from django.urls import path
from Autenticacion import views
from Autenticacion.views import vistaRegistro, cerrarSesion, logear


urlpatterns = [
    path('', views.vistaRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrarSesion, name="cerrar_sesion"),
    path('login', logear, name="login"),
]