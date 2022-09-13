from bookFaceApp.models.inventario import inventory
from rest_framework import serializers

class inventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = ['idInventory']