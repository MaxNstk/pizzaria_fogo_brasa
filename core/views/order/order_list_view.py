from core.models.order import Order
from core.views.generic.generic_list_view import GenericListView
from django.views.generic import ListView

class OrderListView(ListView):

    # todo mudar template para customer
    customer_template = 'order_list.html'
    admin_template = 'order_list.html'

    def get_template_names(self):
        return [self.admin_template] if self.request.user.is_superuser else [self.customer_template]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(customer=self.request.customer)