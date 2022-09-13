from bookFaceApp.models.products import products
from rest_framework import serializers

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['idproducts','name_prod','author','editorial','category','tipoProducto','num_page','isbn','state','rank','formato','presentation','image','price','visits','description','cantidadExistencia','ventas']