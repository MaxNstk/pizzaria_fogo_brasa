from core.models.order import Order
from core.views.generic.generic_list_view import GenericListView
from django.views.generic import ListView

class OrderListView(ListView):

    template_name = 'order_list.html'
    
    def get_queryset(self):
        a = Order.objects.all()
        for p in a:
            pizza_list = []
            for pizza in p.pizzas.all():
                pizza_list.append(f'{pizza.flavor.name} - {pizza.size.short_name}')
            p.__setattr__('pizza_list', pizza_list)
        return Order.objects.all()


    def set_breadcrumbs(self):
        return 'Pedidos > Listagem'