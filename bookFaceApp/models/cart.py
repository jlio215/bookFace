from unittest.util import _MAX_LENGTH
from django.db import models
from .user import User
from .sales import Sales

# Create your models here.
class Cart(models.Model):
    cart = models.CharField('Sesion', max_length=100, unique=True)
    status = models.CharField('Status', max_length=45)
    creationAt = models.DateField()
    updateAt = models.DateTimeField()
    price = models.DecimalField( max_digits = 5, decimal_places = 2)
    discount = models.DecimalField( max_digits = 5, decimal_places = 2)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sales,  on_delete=models.CASCADE)