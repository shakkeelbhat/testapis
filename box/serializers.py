from rest_framework import serializers
from .models import BoxModel
class registerSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    username = serializers.CharField()
    password   = serializers.CharField() 

class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password   = serializers.CharField() 

class boxSerializer(serializers.ModelSerializer):
    class Meta:

        model = BoxModel
        fields ='__all__'
