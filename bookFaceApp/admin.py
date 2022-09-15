from django.contrib import admin
from bookFaceApp.models.products import products

from .models.user import User
from .models.inventory import Inventory
from .models.products import products
from .models.sales import sales
from .models.cart import Cart

# Register your models here.

admin.site.register(Inventory)
admin.site.register(sales)
admin.site.register(User)
admin.site.register(products)
admin.site.register(Cart)