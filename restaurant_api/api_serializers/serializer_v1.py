from rest_framework import serializers
from restaurant_api.models import Restaurant, Grade


class RestaurantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class GradeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'



