from django.views.generic.list import ListView
from django.db.models import Q

from .models import Restaurant, Grade


class MainPageListView(ListView):
    model = Restaurant
    paginate_by = 10
    template_name = 'index.html'
    context_object_name = 'list_of_restaurants'
    queryset = Restaurant.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurants'] = Restaurant.objects.all().count()
        context['reviews'] = Grade.objects.all().count()
        context['objects'] = context['reviews'] + context['restaurants']
        return context


class SearchResultListView(MainPageListView):

    def get_queryset(self):
        user_search_request = self.request.GET.get('s')
        result = Restaurant.objects.filter(
            Q(name__icontains=user_search_request) |
            Q(restaurant_uniq_id__icontains=user_search_request) |
            Q(borough__icontains=user_search_request) |
            Q(street__icontains=user_search_request) |
            Q(pk__icontains=user_search_request)
        )
        print(self.request.GET)
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q_restaurant = self.get_queryset()
        context['restaurants'] = q_restaurant.count()
        context['reviews'] = Grade.objects.filter(fk_grade__in=q_restaurant).count()
        context['objects'] = context['reviews'] + context['restaurants']
        return context


class RestaurantListView(ListView):
    model = Restaurant
    paginate_by = 100
    template_name = 'main.html'
    context_object_name = 'list_of_restaurants'
