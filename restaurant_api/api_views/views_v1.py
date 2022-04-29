from rest_framework import viewsets, permissions
from restaurant_api.models import Restaurant, Grade
from restaurant_api.api_serializers.serializer_v1 import RestaurantModelSerializer, GradeModelSerializer


class RestaurantModelViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GradeModelViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


