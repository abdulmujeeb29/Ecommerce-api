from . import views 
from django.urls import path

urlpatterns = [
    path('products', views.ProductList.as_view(), name='product-list'),
    path('create-products', views.ProductCreate.as_view(), name='product-create'),
    path('products/<int:pk>', views.GetProductDetails.as_view(), name='product_detail'),
    path('products/admin/<int:pk>', views.UpdateProduct.as_view(),name='update-product'),
    

]