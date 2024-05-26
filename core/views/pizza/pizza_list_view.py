from core.models.pizza import Pizza
from core.views.generic.generic_list_view import GenericListView


class PizzaListView(GenericListView):

    paginate_by = 10
    template_name = 'pizza_list.html'
    
    def get_queryset(self):
        return Pizza.objects.all()

    def set_table_headers(self):
        return ['Sabor', 'Tamanho', 'Preço', 'Disponível', 'Ações']

    def set_breadcrumbs(self):
        return 'Produto > Listagem'