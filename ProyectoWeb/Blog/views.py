from django.shortcuts import render
from Blog.models import post, categoria

# Create your views here.

#Esta es la vista de la opcion Blog del menu
def blog(request):
    posts = post.objects.all()
    return render (request, "Blog/blog.html",{"posts": posts})


def categoria_post (request, categoria_id):

    categorias = categoria.objects.get(id=categoria_id)
    posts = post.objects.filter(categoria=categorias)
    return render (request, "Blog/categorias.html", {"categoria": categorias, "posts": posts})