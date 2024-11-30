from django.contrib import admin
from Servicios.models import Servicio

# Register your models here.

class servicio_admin (admin.ModelAdmin):
    list_display=("titulo","contenido","created","updated","imagen")
    readonly_fields=("created","updated")



admin.site.register(Servicio, servicio_admin)