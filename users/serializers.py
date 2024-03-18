from rest_framework import serializers 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib import auth 
from django.contrib.auth.hashers import make_password 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
# class LoginSerializer(serializers.ModelSerializer)
#     class Meta:
#         model = User
#         fields = {'username' , 'password'}