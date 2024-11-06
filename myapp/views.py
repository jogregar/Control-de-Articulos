from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articulos, Categorias
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request,"index.html")

def articulos(request):
    articulos = Articulos.objects.all()
    return render(request,"articulos.html", {"articulos":articulos})

def categorias(request):
    datos = Categorias.objects.all()
    return render(request,"categorias.html",{"categorias":datos})

def admincategorias(request, id):
    if id == 0:
        categoria = {
            "id":0,
            "nom_categoria":""
        }
    else:
        categoria = Categorias.objects.get(id=id)
    return render(request, "admincategorias.html", {"categoria":categoria})

def guardarcategoria(request):
    if request.method == "GET":
        return render(request, "admincategorias.html")
    else:
        if int(request.POST["idcategoria"]) == 0:
            Categorias.objects.create(nom_categoria=request.POST["nomcategoria"])
            mensaje = "Categoria Creada"
        else:
            Categorias.objects.filter(id=request.POST["idcategoria"]).update(nom_categoria=request.POST["nomcategoria"])
            mensaje = "Categoria Modificada"
    messages.success(request,mensaje)
    return redirect("/categorias")

def guardararticulo(request):
    if request.method == "GET":
        return render(request, "adminarticulos.html")
    else:
        if int(request.POST["id"]) == 0:
            Articulos.objects.create(nom_articulo=request.POST["nom_articulo"], des_articulo=request.POST["des_articulo"], can_articulo=request.POST["can_articulo"], pre_articulo=request.POST["pre_articulo"], tip_categoria_id=request.POST["tip_categoria"])
            mensaje = "Articulo Creado"
        else:
            Articulos.objects.filter(id=request.POST["id"]).update(nom_articulo=request.POST["nom_articulo"], des_articulo=request.POST["des_articulo"], can_articulo=request.POST["can_articulo"], pre_articulo=request.POST["pre_articulo"], tip_categoria_id=request.POST["tip_categoria"])
            mensaje = "Articulo Modificado"
    messages.success(request,mensaje)
    return redirect("/articulos/")

def eliminarcategoria(request, id):
    Categorias.objects.filter(id=id).delete()
    mensaje = "Categoria Eliminada"
    messages.success(request,mensaje)
    return redirect("/categorias")

def eliminararticulo(request, id):
    Articulos.objects.filter(id=id).delete()
    mensaje = "Articulo Eliminado"
    messages.success(request,mensaje)
    return redirect("/articulos")

def adminarticulos(request, id):
    if id == 0:
        articulo = {
            "id":0,
            "nom_articulo":"",
            "des_articulo":"",
            "can_articulo":0,
            "pre_articulo":0,
            "tip_categoria":0
        }
    else:
        articulo = Articulos.objects.get(id=id)
    categorias = Categorias.objects.all()
    return render(request, "adminarticulos.html", {"articulo":articulo,"categorias":categorias})









