from bookFaceApp.models.compras import Compras
from rest_framework import serializers

class comprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ['idCompras']