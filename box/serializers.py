from rest_framework import serializers
from .models import BoxModel

from django.contrib.auth.models import User
class registerSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    username = serializers.CharField()
    password   = serializers.CharField()


    def validate(self,data) :
        if data["email"]:
            if User.objects.filter(email=data['email']).exusts():
                raise serializers.ValidationError("email already exists")
        if data["username"]:
            if User.objects.filter(email=data['username']).exusts():
                raise serializers.ValidationError("username already exists")
        return data
    def create(self,validated_data):
        user  = User.objects.create(username=validated_data["username"],email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return validated_data
    
    
class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password   = serializers.CharField() 

class boxSerializer(serializers.ModelSerializer):
    class Meta:

        model = BoxModel
        fields ='__all__'
