from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser): #ke thua Abstracuser
# xóa những trường không sử dụng 
    username = None
    last_login = None
    is_staff = None
    is_superuser = None
    
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = "email" #lấy username bằng email(sử dụng email để đăng nhập)
    REQUIRED_FIELDS = []

    