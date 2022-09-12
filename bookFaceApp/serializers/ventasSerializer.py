from bookFaceApp.models.ventas import ventas
from rest_framework import serializers

class ventasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventas
        fields = ['idVentas']