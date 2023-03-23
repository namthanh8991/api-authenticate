from django.contrib import admin
from django.urls import path, include
from .views import UserRegisterView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('register/', UserRegisterView.as_view()), #dang ki nguoi dung
    path('api/login', jwt_views.TokenObtainPairView.as_view(), name='login'), # dang nhap dung jwt_views

]
