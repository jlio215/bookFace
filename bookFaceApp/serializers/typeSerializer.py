from bookFaceApp.models.type import Type
from rest_framework import serializers

class typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['idtype']