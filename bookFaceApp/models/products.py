from django.db import models
from .sales_has_products import ventas
#from .kindproduct import nombretipodeproducto
from .inventario import inventory
from .tipoproducto import product_type
from .sales import ventas

class products(models.Model):
    idproducts = models.AutoField(primary_key=True)
    name_prod = models.CharField(maxlength=90)
    author= models.CharField(maxlength=45)
    editorial= models.CharField(maxlength=45)
    category= models.CharField(maxlength=45)
    type_prod= models.CharField(maxlength=45)
    num_page=models.BigIntegerField()
    isbn= models.CharField(maxlength=45)
    state= models.CharField(maxlength=250)
    rank= models.CharField(maxlength=45)
    formato= models.CharField(maxlength=45)
    presentation= models.CharField(maxlength=45)
    image= models.CharField(maxlength=60)
    price= models.DecimalField(max_digits=6, decimal_places=3)
    visits= models.BigIntegerField()
    description=models.CharField(maxlength=250) 
    tipoProducto = models.ForeignKey(product_type, related_name='tipo_producto', on_delete=models.CASCADE)
    cantidadExistencia = models.ForeignKey(inventory, related_name='existencias', on_delete=models.CASCADE)    
    ventas = models.ForeignKey(ventas, related_name='ventas', on_delete=models.CASCADE)
    #products = models.ForeignKey(products_has_categories, related_name='idproducts', on_delete=models.CASCADE)
    #idAccount = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    #idAccount = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
