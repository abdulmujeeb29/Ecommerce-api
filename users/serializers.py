from rest_framework import serializers 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib import auth 
from django.contrib.auth.hashers import make_password 
from .models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password' ,'first_name','last_name')
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        # Remove password from validated_data to avoid changing it unless provided
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        # Update other fields normally
        return super().update(instance, validated_data)
    
class AddressSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source ='user.username')
    class Meta:
        model = Address
        fields = '__all__'
    
