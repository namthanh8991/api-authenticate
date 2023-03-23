from django.shortcuts import render
from .models import CarModel
from rest_framework.views import APIView
from .models import CarModel
from .serializer import CarSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CarView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated] #quyen cua nguoi dung
    def get(self, request):
        a = CarModel.objects.all()
        serializer = CarSerializer(a , many = True)
        return Response(serializer.data)
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'them vao thanh cong'}, status=status.HTTP_200_OK)
        else :
            return Response({'message': 'them vao that bai'}, status=status.HTTP_400_BAD_REQUEST)        
    
    
class UpdateCarView(APIView):
    def put(self, request, Khoa_chinh):
        id = Khoa_chinh
        a = CarModel.objects.get(pk= id)
        serializer = CarSerializer(a , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'update thanh cong'}, status=status.HTTP_202_ACCEPTED)
        else :
            return Response({'message':'update that bai '}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, Khoa_chinh):
        id = Khoa_chinh
        a = CarModel.objects.get(pk = id)
        a.delete()
        return Response({'message':'da xoa thanh cong'}, status=status.HTTP_200_OK)
        
            