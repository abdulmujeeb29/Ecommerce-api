from django.shortcuts import render
from .models import *
from rest_framework import generics 
from rest_framework.permissions import *
from .serializers import *
from users.permissions import IsObjectOwner
# Create your views here.

class ListCreateOrder(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrdersSerializer



class GetPutDelOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated,IsObjectOwner]
    serializer_class = OrdersSerializer


