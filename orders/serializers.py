from rest_framework import serializers
from .models import * 



class OrdersSerializer(serializers.ModelSerializer):
    user  = serializers.PrimaryKeyRelatedField( read_only=True)
    
    class Meta:
        model = Orders
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product_name', 'quantity', 'price']