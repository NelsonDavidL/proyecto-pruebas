from django.db import models

# Create your models here.

class categoria (models.Model):

    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class producto (models.Model):

    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE)
    precio=models.IntegerField()
    disponibilidad=models.BooleanField(default=True)
    descripcion=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__ (self):
        return self.nombre