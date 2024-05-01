from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListCreateOrder.as_view(),name='get-post-order'),
    path('<int:pk>',views.GetPutDelOrder.as_view(),name='get-pul-orders'),
    path('api/orders/<int:order_id>/items/', views.OrderItemsListView.as_view(), name='order-items-list'),
    path('api/orders/<int:order_id>/items/add/', views.AddOrderItemView.as_view(), name='add-order-item'),

]