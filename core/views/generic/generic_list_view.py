from django.views.generic import ListView


class GenericListView(ListView):

    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['headers'] = self.set_table_headers()
        return context
    
    def set_table_headers(self):
        return None
