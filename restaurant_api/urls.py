from django.urls import path, include
from rest_framework import routers
from restaurant_api.api_views.views_v1 import RestaurantModelViewSet, GradeModelViewSet

from restaurant_api.api_views.views_v2 import RestaurantAPIView, GradeAPIView


router_v1 = routers.DefaultRouter()
router_v1.register(r'restaurant', RestaurantModelViewSet)
router_v1.register(r'grade', GradeModelViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),

    path('v2/grade/', GradeAPIView.as_view()),
    path('v2/restaurant/', RestaurantAPIView.as_view()),

]
