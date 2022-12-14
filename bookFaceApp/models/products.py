from django.db import models
from .inventory import Inventory
from .sales import Sales
from .user import User

class products(models.Model):
    product = models.AutoField(primary_key=True)
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
    inventory = models.ForeignKey(Inventory,  on_delete=models.CASCADE)    
    sale=models.ForeignKey(Sales,  on_delete=models.CASCADE)
    user=models.ForeignKey(User,  on_delete=models.CASCADE) 

