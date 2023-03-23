from django.contrib import admin
from django.urls import path, include
from .views import CarView, UpdateCarView
urlpatterns = [
    path('car', CarView.as_view() ),
    path('update/<int:Khoa_chinh>', UpdateCarView.as_view())

]
