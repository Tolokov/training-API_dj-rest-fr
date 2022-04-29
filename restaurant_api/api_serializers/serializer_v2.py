from rest_framework import serializers
from restaurant_api.models import Grade, Restaurant

class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    uniq = serializers.IntegerField(source='restaurant_uniq_id')
    borough = serializers.CharField(max_length=300)
    cuisine = serializers.CharField(max_length=300)
    building = serializers.CharField(max_length=15)
    street = serializers.CharField(max_length=500)
    zipcode = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()


class GradeSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True, required=False)
    fk = serializers.CharField(source='fk_grade', allow_null=True)
    date = serializers.DateTimeField(required=False)
    grade = serializers.CharField(max_length=2)
    score = serializers.IntegerField()

    def create(self, data):
        return Grade.objects.create(**data)
