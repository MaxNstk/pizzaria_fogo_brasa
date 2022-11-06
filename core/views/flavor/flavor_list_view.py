from core.models.flavor import Flavor
from core.views.generic.generic_list_view import GenericListView


class FlavorListView(GenericListView):

    template_name = 'flavor_list.html'

    def get_queryset(self):
        return Flavor.objects.all()

    def set_table_headers(self):
        return ['Nome', 'Descrição', 'Disponível', 'Ações']

    def set_breadcrumbs(self):
        return 'Sabor > Listagem'