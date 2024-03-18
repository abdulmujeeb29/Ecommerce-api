from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from django.contrib.auth import login , authenticate ,logout
from django.contrib import auth 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data = request.data )
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED )
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_users(request):  
    data = User.objects.all()
    serializer = UserSerializer(data,many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK )
    

class LoginView(APIView):
    def post(self , request, format='json'):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh' : str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        
        else :
            return Response({'error' : 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'error' : 'Username or passsword missing'}, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['POST'])
def logout_view(request):
    user = request.user 
    if request.method == 'POST':
        if user.is_authenticated:
            logout(request)
            return Response('logout Successful', status=status.HTTP_200_OK)
        
    return Response('issue')