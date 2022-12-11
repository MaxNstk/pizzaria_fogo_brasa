from django.urls import reverse_lazy
from django.views.generic import CreateView
from core.forms.order_form import OrderForm

class OrderCreateView(CreateView):

    template_name = 'order_form.html'
    form_class = OrderForm

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str: 
        return reverse_lazy('home')
