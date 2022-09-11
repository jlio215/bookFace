from unittest.util import _MAX_LENGTH
from django.db import models
from .carritocompras import Cart

# Create your models here.

class Cartitem(models.Model):
    sku = models.CharField('Sesion', max_length=45, unique=True)
    price = models.DecimalField('Price', max_length=20)
    descuento = models.DecimalField('Descuento', max_len=10)
    cantidad = models.IntegerField('Cantidad', max_length=10)
    fechacreacion = models.DateField('FechaCreacion', max_length=16)
    fechaactualizacion = models.DateField('FechaActualizacion', max_length=16)
    carritocompras = models.ForeignKey(Cart, related_name='cartItem', on_delete=models.CASCADE)
