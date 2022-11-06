from django.urls import reverse_lazy
from django.views.generic import UpdateView

class GenericUpdateView(UpdateView):

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return reverse_lazy(f'{self.model._meta.model_name}_list')
