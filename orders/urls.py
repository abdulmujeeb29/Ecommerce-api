from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListCreateOrder.as_view(),name='get-post-order'),
    path('<int:pk>',views.GetPutDelOrder.as_view(),name='get-pul-orders'),

]