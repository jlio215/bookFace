from bookFaceApp.models import tipoproducto
from bookFaceApp.models.tipoproducto import product_type
from rest_framework import serializers

class tipoproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoproducto
        fields = ['idproduct_type']