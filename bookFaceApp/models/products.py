from django.db import models
#from .kindproduct import nombretipodeproducto
from .inventario import inventory
#from .tipoproducto import product_type
from .ventas import ventas
from .user import User

class products(models.Model):
    idproducts = models.AutoField(primary_key=True)
    name_prod = models.CharField(max_length=90)
    author= models.CharField(max_length=45)
    editorial= models.CharField(max_length=45)
    category= models.CharField(max_length=45)
    type_prod= models.CharField(max_length=45)
    num_page=models.BigIntegerField()
    isbn= models.CharField(max_length=45)
    state= models.CharField(max_length=250)
    rank= models.CharField(max_length=45)
    format_prod= models.CharField(max_length=45)
    presentation= models.CharField(max_length=45)
    image= models.CharField(max_length=60)
    price= models.DecimalField(max_digits=6, decimal_places=3)
    visits= models.BigIntegerField()
    description=models.CharField(max_length=250) 
    name_cat=models.CharField(max_length=45)
    subcategory=models.CharField(max_length=45)
    amount = models.ForeignKey(inventory, related_name='existencias', on_delete=models.CASCADE)    
    stock_prod=models.ForeignKey(ventas, related_name='ventas', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='usuaario', on_delete=models.CASCADE) 
    #tipoProducto = models.ForeignKey(product_type, related_name='tipo_producto', on_delete=models.CASCADE)
    #ventas = models.ForeignKey(ventas, related_name='ventas', on_delete=models.CASCADE)