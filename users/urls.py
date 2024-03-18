from . import views 
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns =[
    path('get-users',views.list_users,name="list-user"),
    path('auth/register',views.register,name="register-user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login',views.LoginView.as_view(),name="login"),
    path('logout',views.logout_view,name='logout')

]