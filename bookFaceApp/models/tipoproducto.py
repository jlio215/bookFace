from django.db import models
from.user import User

class product_type(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipoProducto = models.CharField(max_length=60)