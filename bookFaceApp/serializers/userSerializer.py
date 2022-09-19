#from itertools import product
from rest_framework import serializers
from bookFaceApp.models.user import User
#from bookFaceApp.models.account import Account
#from bookFaceApp.serializers.accountSerializer import AccountSerializer
#from bookFaceApp.models.products import products
#from bookFaceApp.serializers.productSerializer import productSerializer


class UserSerializer(serializers.ModelSerializer):
    #account = AccountSerializer()
    #type = TypeSerializer()
    class Meta:
        model = User 
        fields = ['id', 'username', 'password', 'name', 'email', 'idtype', 'idnumber', 'city', 'address']#, 'account']

    def create(self, validated_data):
        #accountData = validated_data.pop('account')
        #typeData = validated_data.pop('type')
        userInstance = User.objects.create(**validated_data)
        #Account.objects.create(user=userInstance, **accountData)
        return userInstance


    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        #account = Account.objects.get(user=obj.id)
        #type = Type.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'idtype': user.idtype,
                    'idnumber': user.idnumber,
                    'city': user.city,
                    'address': user.address,
                    #'account': {
                    #            'id': account.id,
                    #            'balance': account.balance,
                    #            'lastChangeDate': account.lastChangeDate,
                    #            'isActive': account.isActive
                    #            }    
                    

         }

  
 
