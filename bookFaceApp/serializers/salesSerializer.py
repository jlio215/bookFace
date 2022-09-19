from bookFaceApp.models.sales import Sales
from rest_framework import serializers

class salesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['sales', 'dateSales', 'amount', 'totalOrder']