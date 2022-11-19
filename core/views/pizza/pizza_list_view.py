from core.models.pizza import Pizza
from django.views.generic import ListView


class PizzaListView(ListView):

    paginate_by = 10
    template_name = 'pizza_list.html'
    
    def get_queryset(self):
        return Pizza.objects.all()