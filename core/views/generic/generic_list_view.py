from django.views.generic import ListView
from django.core.paginator import Paginator


class GenericListView(ListView):

    entries_per_page = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['headers'] = self.set_table_headers()

        paginator = Paginator(self.get_queryset(), self.entries_per_page)
        page_number = self.request.GET.get('page', 1)
        context['page_obj'] = paginator.get_page(page_number)
        return context

    def set_table_headers(self):
        return None
    