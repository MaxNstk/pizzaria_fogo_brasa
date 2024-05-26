from django.urls import reverse_lazy
from django.views.generic import UpdateView

from core.mixins.dispatch_user_mixin import UserDispatchMixin

class GenericUpdateView(UserDispatchMixin, UpdateView):
    
    def get_success_url(self) -> str:
        return reverse_lazy(f'{self.model._meta.model_name}_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['breadcrumbs'] = self.set_breadcrumbs()
        return context

    def set_breadcrumbs(self):
        return ''