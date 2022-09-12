from bookFaceApp.models.categoria import categoria
from rest_framework import serializers

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ['idCategoria']