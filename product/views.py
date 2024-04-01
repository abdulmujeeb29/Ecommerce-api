from django.shortcuts import render
from rest_framework import generics ,permissions ,status 
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response 
from rest_framework.views import APIView
# Create your views here.


# class CommonProductPermission:

#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return AllowAny()
        
#         return IsAdminUser()


    


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    permission_classes = [AllowAny]

    
class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    permission_classes = [IsAdminUser]

    
class GetProductDetails(APIView):
    permission_classes = [AllowAny]

    def get(self , request , pk , format='json'):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)


class UpdateProduct(APIView):
    permission_classes = [IsAdminUser]

    def put(self , request , pk ,format=None):
        product =Product.objects.get(id=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request , pk , format=None):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'response': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response({'response': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    

class ProductReviewsList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retrieve reviews for a specific product.
        """
        product = self.get_object_or_404(Product, pk=self.kwargs['pk'])    #we used get_object_or_404 in place of the try except block 
        
        return Review.objects.filter(product=product)

class ProductReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Submit a review for a specific product.
        """
        product = self.get_object_or_404(Product, pk=self.kwargs['pk'])
        request.data['product'] = product.id  # Use product.id instead of pk for clarity
        request.data['user'] = request.user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)