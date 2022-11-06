from django.views.generic import ListView
from django.utils.translation import gettext as _


class GenericListView(ListView):

    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['headers'] = self.set_table_headers()
        context['breadcrumbs'] = self.set_breadcrumbs()
        return context
    
    def set_table_headers(self):
        return None

    def set_breadcrumbs(self):
        return ''
