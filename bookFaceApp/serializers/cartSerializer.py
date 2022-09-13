from bookFaceApp.models.carritocompras import Cart
from rest_framework import serializers

class carritocomprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['idCart']