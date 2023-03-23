from rest_framework import serializers
from .models import CarModel
class CarSerializer(serializers.ModelSerializer):
    class Meta :
        model = CarModel
        fields = ('name', 'brand', 'color', 'id')
        