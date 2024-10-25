from django.shortcuts import render, redirect
from .models import Articulo, Categoria
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, "articulos.html", {"articulos":articulos})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {"categorias":categorias}) 

def saludo(request, datos):
    return render(request, "saludo.html", {"datos":datos})

def adminarticulo(request, id):
    if (id != 0):
        articulo = Articulo.objects.get(id=id)
    else:
        articulo = {
            "id":0,
            "nom_articulo":"",
            "des_articulo":"",
            "can_articulo":"",
            "pre_articulo":"",
            "cat_articulo_id":""
        }
    categorias = Categoria.objects.all()
    return render(request, "adminarticulos.html" , {"art":articulo, "categorias":categorias} )

def admincategorias(request, id):
    if (id != 0):
        categoria = Categoria.objects.get(id=id)
    else:
        categoria = {
            "id":0,
            "nom_categoria":"",
        }
    return render(request, "admincategorias.html" , {"categoria":categoria} )

def creararticulo(request):
    if request.method == "GET":
        return render(request, "adminarticulos.html")
    else:
        # if isinstance(request.POST["id"], (int)):
        #     id = request.POST["id"]
        # else:
        #     id = int(request.POST["id"])    
        if int(request.POST["id"]) == 0:
            Articulo.objects.create(nom_articulo=request.POST["nombre"], des_articulo=request.POST["descripcion"], can_articulo=request.POST["cantidad"], pre_articulo=request.POST["precio"], cat_articulo_id=request.POST["opciones"])
            mensaje = "Articulo Guardado"
        else:
            Articulo.objects.filter(id=request.POST["id"]).update(nom_articulo=request.POST["nombre"], des_articulo=request.POST["descripcion"], can_articulo=request.POST["cantidad"], pre_articulo=request.POST["precio"], cat_articulo_id=request.POST["opciones"])
            mensaje = "Articulo Modificado"
        messages.success(request,mensaje)
        return redirect("/articulos/")

def crearcategoria(request):
    if request.method == "GET":
        return render(request, "admincategorias.html")
    else:
        # if isinstance(request.POST["id"], (int)):
        #     id = request.POST["id"]
        # else:
        #     id = int(request.POST["id"]) 
        if int(request.POST["id"]) == 0:
            Categoria.objects.create(nom_categoria=request.POST["nombre"])
            mensaje = "Categoria Guardada"
        else:
            Categoria.objects.filter(id=request.POST["id"]).update(nom_categoria=request.POST["nombre"])
            mensaje = "Categoria Modificada"
        messages.success(request,mensaje)
        return redirect("/categorias/")

def eliminararticulo(request, id):
    Articulo.objects.filter(id=id).delete()
    mensaje = "Articulo Eliminado"
    messages.success(request,mensaje)
    return redirect("/articulos/")

def eliminarcategoria(request, id):
    Categoria.objects.filter(id=id).delete()
    mensaje = "Categoria Eliminada"
    messages.success(request,mensaje)
    return redirect("/categorias/")
