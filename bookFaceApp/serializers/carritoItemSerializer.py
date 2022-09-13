from bookFaceApp.models.carritoitems import Cartitem
from rest_framework import serializers

class carritoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitem
        fields = ['idCartitem']