from django.contrib import admin
from django.urls import path, include

from restaurant_api.views import SearchResultListView, MainPageListView, RestaurantListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageListView.as_view(), name='index'),
    path('main/', RestaurantListView.as_view(), name='main'),
    path('search', SearchResultListView.as_view(), name='search'),
    path('api/', include('restaurant_api.urls')),
]




