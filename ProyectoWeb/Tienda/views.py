from django.shortcuts import render
from .models import producto, categoria
# Create your views here.

#Esta es la vista de la opcion Tienda del menu
def tienda(request):
    productos = producto.objects.all()
    return render (request, "Tienda/tienda.html",{"productos":productos})

def categoria_prod (request, categoria_id):
    pass