from core.models.size import Size
from core.views.generic.generic_list_view import GenericListView


class SizeListView(GenericListView):

    template_name = 'size_list.html'
    
    def get_queryset(self):
        return Size.objects.all()

    def set_table_headers(self):
        return ['Sigla', 'Descrição', 'Disponível', 'Editar']
