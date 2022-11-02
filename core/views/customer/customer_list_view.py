from core.models.user import User
from core.views.generic.generic_list_view import GenericListView


class CustomerListView(GenericListView):

    template_name = 'customer_list.html'
    
    def get_queryset(self):
        return User.objects.all()

    def set_table_headers(self):
        return ['Nome', 'CPF', 'E-mail', 'Editar']
