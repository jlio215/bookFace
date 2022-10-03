from rest_framework import serializers
from bookFaceApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance


    def to_representation(self, obj):
        user = User.objects.get(user=obj.user)
        return {
                    'user': user.user,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'idtype': user.idtype,
                    'idnumber': user.idnumber,
                    'city': user.city,
                    'address': user.address,
         }

 
