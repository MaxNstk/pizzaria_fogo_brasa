from core.models.product import Product
from core.views.generic.generic_list_view import GenericListView


class ProductListView(GenericListView):

    template_name = 'product_list.html'
    
    def get_queryset(self):
        return Product.objects.all()

    def set_table_headers(self):
        return ['Descrição', 'Preço', 'Disponível', 'Ações']

    def set_breadcrumbs(self):
        return 'Produto > Listagem'