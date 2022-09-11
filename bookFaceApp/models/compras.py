from unittest.util import _MAX_LENGTH
from django.db import models
from .user import User
from .products import products

class Compras(models.Model):
    username = models.ForeignKey(User, related_name='idUser', on_delete=models.CASCADE)
    idproducts = models.ForeignKey(products, related_name='idProducts', on_delete=models.CASCADE)

