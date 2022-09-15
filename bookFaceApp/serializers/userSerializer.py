from itertools import product
from rest_framework import serializers
from bookFaceApp.models.user import User
from bookFaceApp.models.products import products
from bookFaceApp.serializers.productSerializer import productSerializer


class UserSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    class Meta:
        model = User 
        fields = ['id', 'username', 'password', 'name', 'email', 'idtype', 'idnumber', 'city', 'address', 'type']

    def create(self, validated_data):
        typeData = validated_data.pop('type')
        userInstance = User.objects.create(**validated_data)
        Type.objects.create(user=userInstance, **typeData)
        return userInstance


    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        type = Type.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'idtype': user.idtype,
                    'idnumber': user.idnumber,
                    'city': user.city,
                    'address': user.address,
                    'type': {
                        'id': type.id,
                        'user_role': type.user_role,
                        'right': type.right,
                        'logs': type.logs

         }

}   
 
