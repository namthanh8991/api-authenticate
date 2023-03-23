from django.db import models

# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=60)
    brand = models.CharField(max_length=20)