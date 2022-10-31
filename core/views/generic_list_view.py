from multiprocessing import context
from django.views.generic import ListView

class GenericListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headers'] = self.set_table_headers()
        return context

    def set_table_headers(self):
        return None
