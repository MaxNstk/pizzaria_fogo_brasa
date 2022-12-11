from core.models.order import Order
from core.views.generic.generic_list_view import GenericListView


class OrderListView(GenericListView):

    paginate_by = 10
    template_name = 'order_list.html'
    
    def get_queryset(self):
        return Order.objects.all()

    def set_table_headers(self):
        return ['Pedido', 'Descrição', 'Observações', 'Total','Status', 'Ações']

    def set_breadcrumbs(self):
        return 'Pedidos > Listagem'