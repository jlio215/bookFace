from bookFaceApp.models.cart import Cart
from rest_framework import serializers

class carritocomprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['sessionId','status','creationAt','updateAt','price','discount','quantity']