from django.db import models
from .user import User

class ventas(models.Model):
    idVentas = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(default=0)
    fechaVenta = models.DateTimeField()