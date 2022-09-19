from bookFaceApp.models.cart import Cart
from rest_framework import serializers

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['cart','status','creationAt','updateAt','price','discount','quantity']