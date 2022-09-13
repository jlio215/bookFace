from itertools import product
from rest_framework import serializers
from bookFaceApp.models.user import User
from bookFaceApp.models.products import products
from bookFaceApp.serializers.productSerializer import productSerializer

class UserSerializer(serializers.ModelSerializer):
    product = productoSerializer()

class Meta:
    model = User
    fields = ['id', 'username', 'password', 'name', 'email']

def create(self, validated_data):
    productData = validated_data.pop('product')
    userInstance = User.objects.create(**validated_data)
    products.objects.create(user=userInstance, **productData)
    return userInstance

def to_representation(self, obj):
    user = User.objects.get(id=obj.id)
    products = products.objects.get(user=obj.id)
    return {
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'product': {
        'id': products.id,
        'balance': products.balance,
        'lastChangeDate': products.lastChangeDate,
        'isActive': products.isActive
}
}