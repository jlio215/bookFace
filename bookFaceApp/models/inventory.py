from django.db import models
from .user import User

class Inventory(models.Model):
    inventory = models.BigAutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    isbn = models.CharField(max_length=45)
    purchasedQuantity = models.IntegerField(default=0)
    soldQuantity = models.IntegerField(default=0)