from django.shortcuts import render,redirect
from .forms import formulario_contacto
from django.core.mail import send_mail, EmailMessage

# Create your views here.

#Esta es la vista de la opcion Contacto del menu
def contacto(request):
    formularioContacto=formulario_contacto()

    if request.method=="POST":
        formularioContacto=formulario_contacto(data=request.POST)
        if formularioContacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")

            enviaremail=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {}, con la direccion {}, te escribe lo siguiente: \n\n {}".format(nombre,email,mensaje),
            "nelsonpruebas@outlook.es",["nelson875413@gmail.com"])
            try:
                enviaremail.send()
            
            #send_mail(nombre["nombre"],mensaje["Mensaje"],email.get("Email",""),['nelson875413@gmail.com'],)

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render (request, "Contacto/contacto.html", {"miFormulario": formularioContacto})