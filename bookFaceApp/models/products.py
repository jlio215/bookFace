from django.db import models
#from .kindproduct import nombretipodeproducto
from .inventario import inventory
from .tipoproducto import product_type
from .ventas import ventas

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
    formato= models.CharField(max_length=45)
    presentation= models.CharField(max_length=45)
    image= models.CharField(max_length=60)
    price= models.DecimalField(max_digits=6, decimal_places=3)
    visits= models.BigIntegerField()
    description=models.CharField(max_length=250) 
    tipoProducto = models.ForeignKey(product_type, related_name='tipo_producto', on_delete=models.CASCADE)
    cantidadExistencia = models.ForeignKey(inventory, related_name='existencias', on_delete=models.CASCADE)    
    ventas = models.ForeignKey(ventas, related_name='ventas', on_delete=models.CASCADE)
    #products = models.ForeignKey(products_has_categories, related_name='idproducts', on_delete=models.CASCADE)
    #idAccount = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    #idAccount = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
