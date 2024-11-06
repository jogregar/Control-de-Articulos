from django.db import models

# Create your models here.

class Categorias(models.Model):
    nom_categoria = models.CharField(max_length=50)

class Articulos(models.Model):
    nom_articulo = models.CharField(max_length=50)
    des_articulo = models.CharField(max_length=100)
    can_articulo = models.IntegerField()
    pre_articulo = models.FloatField()
    tip_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

