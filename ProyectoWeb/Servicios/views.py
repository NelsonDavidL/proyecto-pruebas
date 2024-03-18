from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.

#Esta es la vista de la opcion Servicios del menu
def servicios(request):
    #Variable donde se almacenan los objetos del modelo Servicio en el archivo models de la app Servicios
    servicios = Servicio.objects.all()
    return render (request, "Servicios/servicios.html", {"servicios": servicios})
