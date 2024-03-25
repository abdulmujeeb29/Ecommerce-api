from django.shortcuts import render
from rest_framework import generics ,permissions 
from rest_framework.permissions import AllowAny,IsAdminUser
from .models import *
from .serializers import *
# Create your views here.


class CommonProductPermission:

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny()
        
        return IsAdminUser()


    


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    permission_classes = [CommonProductPermission]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CommonProductPermission]

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return permissions.AllowAny()
        
    #     return permissions.IsAdminUser()