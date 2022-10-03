from django.db import models

class Sales(models.Model):
    sale = models.AutoField(primary_key=True)
    dateSales = models.DateTimeField()
    amount = models.IntegerField(default=0)
    totalOrder = models.DecimalField( max_digits = 5, decimal_places = 2)
    
    