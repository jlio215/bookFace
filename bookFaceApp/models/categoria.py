from django.db import models
from .user import User

class categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    idAccount = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    nombreCategoria = models.CharField(maxlength=30)
    subCategoria = models.CharField(maxlength=30)
    