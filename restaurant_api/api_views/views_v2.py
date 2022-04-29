from restaurant_api.api_serializers.serializer_v2 import RestaurantSerializer, GradeSerializer
from rest_framework import views, permissions
from restaurant_api.models import Restaurant, Grade
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class RestLimitOffsetPagination(LimitOffsetPagination):
# class RestLimitOffsetPagination(PageNumberPagination):
# class RestLimitOffsetPagination(CursorPagination):

    default_limit = 1


class RestaurantAPIView(views.APIView):

    paginate_class = RestLimitOffsetPagination()

    def get(self, request):
        queryset = Restaurant.objects.all()
        page = self.paginate_class.paginate_queryset(queryset, request)
        serializer_for_queryset = RestaurantSerializer(instance=page, many=True)
        return Response(serializer_for_queryset.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class GradeAPIView(views.APIView):

    paginate_class = RestLimitOffsetPagination()

    def get(self, request):
        queryset = Grade.objects.all()
        page = self.paginate_class.paginate_queryset(queryset, request)
        serializer_for_queryset = GradeSerializer(instance=page, many=True)
        return Response(serializer_for_queryset.data)


    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

