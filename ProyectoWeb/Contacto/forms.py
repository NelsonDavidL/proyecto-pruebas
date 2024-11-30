from django import forms

class formulario_contacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="Email", required=True)
    mensaje=forms.CharField(label="Mensaje", widget=forms.Textarea)