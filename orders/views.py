from django.shortcuts import render
from .models import *
from rest_framework import generics 
from rest_framework.permissions import *
from .serializers import *
# Create your views here.

class ListCreateOrder(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrdersSerializer