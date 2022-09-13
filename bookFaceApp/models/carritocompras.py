from unittest.util import _MAX_LENGTH
from django.db import models
from .user import User

# Create your models here.
class Cart(models.Model):
    idCart = models.BigAutoField(primary_key=True)
    status = models.CharField('Status', max_length=45)
    fechaCreacion = models.DateTimeField()
    fechaActualizacion = models.DateTimeField()
    idUser = models.ForeignKey(User, related_name='userIds', on_delete=models.CASCADE)