from unittest.util import _MAX_LENGTH
from django.db import models
from .user import User

# Create your models here.
class Cart(models.Model):
    sessionid = models.CharField('Sesion', max_length=100, unique=True)
    status = models.CharField('Status', max_length=45)
    fechacreacion = models.DateField('FechaCreacion', max_length=16)
    fechaactualizacion = models.DateField('FechaActualizacion', max_length=16)
    username = models.ForeignKey(User, related_name='id', on_delete=models.CASCADE)