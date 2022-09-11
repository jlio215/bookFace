from django.db import models
from .user import User

class inventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    cantidadExistencia = models.IntegerField(default=0)
    cantidadComprada = models.IntegerField(default=0)
    cantidadvendida = models.IntegerField(default=0)
    fechaCompraInicial = models.IntegerField(default=0)   