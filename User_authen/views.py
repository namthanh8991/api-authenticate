from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from Car import settings
from .serializer import UserSerializer, UserLoginSerializer
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
# Create your views here.
class UserRegisterView(APIView): #dang ki tai khoan
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password']) # mã hóa mật khẩu dùng makepassword
            serializer.save()
            return JsonResponse({'message':'register successfull'}, status= status.HTTP_200_OK)
        else :
            return JsonResponse({'message':'regisster not successfull'}, status= status.HTTP_400_BAD_REQUEST)
        
        
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username = serializer.validate['email'], password = serializer.validate['password'])
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'access_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
                    'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response({
                'message':'email or password is incorrect'
                
                
            },status=status.HTTP_400_BAD_REQUEST)
        return Response({  
                'message':'serializer.errors'
            
        }, status=status.HTTP_400_BAD_REQUEST)