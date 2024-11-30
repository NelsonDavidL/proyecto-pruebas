from django.contrib import admin
from .models import categoria, producto

# Register your models here.

class categoria_admin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class producto_admin(admin.ModelAdmin):
    list_display=("nombre","categoria","precio","descripcion","disponibilidad","created","updated")
    readonly_fields=("created","updated")


admin.site.register(categoria, categoria_admin)
admin.site.register(producto, producto_admin)

