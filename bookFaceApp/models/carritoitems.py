from unittest.util import _MAX_LENGTH
from django.db import models
from .carritocompras import Cart

# Create your models here.

class Cartitem(models.Model):
    idCarItem = models.BigAutoField(primary_key=True)
    price = models.IntegerField(default=0)
    descuento = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    fechacreacion = models.DateTimeField()
    fechaactualizacion = models.DateTimeField()
    carritocompras = models.ForeignKey(Cart, related_name='cartItem', on_delete=models.CASCADE)
