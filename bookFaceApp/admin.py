from django.contrib import admin
from .models.user import User
from .models.products import Products
from .models.inventory import Inventory
from .models.sales import Sales
from .models.cart import Cart

# Register your models here.

admin.site.register(User)
admin.site.register(Products)
admin.site.register(Inventory)
admin.site.register(Sales)
admin.site.register(Cart)