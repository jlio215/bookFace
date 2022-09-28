from bookFaceApp.models.products import products
from rest_framework import serializers

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'