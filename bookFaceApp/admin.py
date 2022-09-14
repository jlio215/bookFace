from django.contrib import admin
from .models.inventory import Inventory
from .models.sales import sales

# Register your models here.

admin.site.register(Inventory)
admin.site.register(sales)