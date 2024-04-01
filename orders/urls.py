from django.urls import path
from . import views

urlpatterns = [
    path('orders',views.ListCreateOrder.as_view(),name='get-post-order'),

]