from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics , permissions 
from django.contrib.auth import login , authenticate ,logout
from django.contrib import auth 
from rest_framework.permissions import IsAuthenticated , AllowAny ,IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsObjectOwner

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


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request , *args, **kwargs):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')
        
        user = request.user  # Retrieve the authenticated user
        
        # Ensure the user exists and check the old password
        if not user.check_password(old_password):
            return Response({'error': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure new password and confirm password match
        if new_password != confirm_password:
            return Response({'error': 'New password and confirm password do not match.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Set the new password
        user.set_password(new_password)
        user.save()
        
        return Response({'message': 'Password changed successfully.'}, status=status.HTTP_202_ACCEPTED)
        
        
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request ,pk, format=None):

        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserAddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated,IsObjectOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated,IsObjectOwner]






