from django.contrib import admin
from .models import categoria, post

# Register your models here.

class categoria_admin (admin.ModelAdmin):
    #list_display=("nombre","created","updated")
    readonly_fields=("created","updated")

class post_admin (admin.ModelAdmin):
    list_display=("titulo","author","created","updated")
    readonly_fields=("created","updated")

admin.site.register(categoria, categoria_admin)
admin.site.register(post, post_admin)