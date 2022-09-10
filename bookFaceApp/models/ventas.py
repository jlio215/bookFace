from django.db import models
from .user import User

class ventas(models.Model):
    idVentas = models.AutoField(primary_key=True)
    idAccount = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    fechaVenta = models.DateTimeField()
    cantidad = models.IntegerField(default=0)