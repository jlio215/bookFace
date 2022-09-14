from bookFaceApp.models.sales import sales
from rest_framework import serializers

class salesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales
        fields = ['sales', 'dateSales', 'amount', 'totalOrder']