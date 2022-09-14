from bookFaceApp.models.inventory import Inventory
from rest_framework import serializers

class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['inventory', 'quantity', 'isbn', 'purchasedQuantity', 'soldQuantity']