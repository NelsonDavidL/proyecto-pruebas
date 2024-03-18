from django.shortcuts import render, redirect
#Importar clase view de django
from django.views.generic import View
#Importar clase UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.


#Se crea una clase que va a encargarse del GET y POST del formulario (cambiar en el archivo URLS)
class vistaRegistro(View):
    #Funcion para el GET
    def get(self, request):
        #Variable que almacena el formulario de creacion de usuario
        form=UserCreationForm()
        return render (request , "Registro/registro.html",{"form":form})

    #Funcion para el POST
    def post(self, request):

        #Variable que almacena la informacion introducida en el formulario
        form=UserCreationForm(request.POST)

        if form.is_valid():
        #Variable que almacena la informacion del formulario guardada
            usuario=form.save()

            login(request, usuario)

            return redirect ('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render (request , "Registro/registro.html",{"form":form})

def cerrarSesion(request):
    logout(request)
    return redirect ('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request,usuario)
                return redirect ('Home')
            else:
                messages.error(request, "Usuario invalido")
        else:
            messages.error(request, "Informacion incorrecta")        

    form=AuthenticationForm()
    return render (request , "Login/login.html",{"form":form})