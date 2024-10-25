from django.db import models

# Create your models here.

class Categoria(models.Model):
    nom_categoria = models.CharField(max_length=60)

class Articulo(models.Model):
    nom_articulo = models.CharField(max_length=60)
    des_articulo = models.CharField(max_length=100)
    can_articulo = models.IntegerField()
    pre_articulo = models.FloatField()
    cat_articulo = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class TipoTransaccion(models.Model):
    tip_transaccion = models.CharField(max_length=20)

class Transacciones(models.Model):
    id_articulo = models.IntegerField()
    tip_transaccion = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)
    can_transaccion = models.IntegerField()
    fec_transaccion = models.DateField()

