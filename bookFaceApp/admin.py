from django.contrib import admin
from .models.carritocompras import Cart
from .models.carritoitems import Cartitem
from .models.categoria import categoria
from .models.compras import Compras
from .models.inventario import inventory
from .models.products import products
from .models.tipoproducto import product_type
from .models.type import Type
from .models.user import User
from .models.ventas import ventas

# Register your models here.
admin.site.register(User)
admin.site.register(products)
admin.site.register(product_type)
admin.site.register(inventory)
admin.site.register(Cart)
admin.site.register(Cartitem)
admin.site.register(categoria)
admin.site.register(Compras)
admin.site.register(Type)
admin.site.register(ventas)
