from bookFaceApp.models.products import products
from rest_framework import serializers

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['idproduct']