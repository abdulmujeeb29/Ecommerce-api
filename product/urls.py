from . import views 
from django.urls import path

urlpatterns = [
    path('products', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail')

]