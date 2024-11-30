from django.shortcuts import render, HttpResponse



# Create your views here.

#Esta es la vista de la opcion Inicio del menu
def home(request):
    return render (request, "ProyectoWebApp/home.html")





