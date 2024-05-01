from django.shortcuts import render
from .models import *
from rest_framework import generics 
from rest_framework.permissions import *
from .serializers import *
from users.permissions import IsObjectOwner
from django.shortcuts import get_object_or_404
# Create your views here.

class ListCreateOrder(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrdersSerializer



class GetPutDelOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated,IsObjectOwner]
    serializer_class = OrdersSerializer


#list items in an order 
class OrderItemsListView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return OrderItem.objects.filter(order_id=order_id)
    

#Add items to a specific order.
class AddOrderItemView(generics.CreateAPIView):        
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order_id = self.kwargs['order_id']
        order = get_object_or_404(Orders, pk=order_id)
        serializer.save(order=order)

# Update quantity of an item in a specific order.

class UpdateOrderItemView(generics.UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order_id = self.kwargs['order_id']
        item_id = self.kwargs['item_id']
        return get_object_or_404(OrderItem, order_id=order_id, pk=item_id)

# Remove an item from a specific order.

class DeleteOrderItemView(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order_id = self.kwargs['order_id']
        item_id = self.kwargs['item_id']
        return get_object_or_404(OrderItem, order_id=order_id, pk=item_id)

# class UpdateOrderItemView(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, order_id, item_id):
#         order_item = get_object_or_404(OrderItem, order_id=order_id, pk=item_id)
#         serializer = OrderItemSerializer(order_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DeleteOrderItemView(APIView):
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, order_id, item_id):
#         order_item = get_object_or_404(OrderItem, order_id=order_id, pk=item_id)
#         order_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)