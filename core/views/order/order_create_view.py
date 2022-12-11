from django.urls import reverse_lazy
from django.views.generic import CreateView
from core.forms.order_form import OrderForm
from core.models.order_pizza import OrderPizza
from core.models.order_product import OrderProduct

class OrderCreateView(CreateView):

    template_name = 'order_form.html'
    form_class = OrderForm

    def form_valid(self, form):
        form.instance.customer = self.request.user
        response = super().form_valid(form)
        for pizza in form.cleaned_data['pizzas']:      
            OrderPizza.objects.create(pizza=pizza, order=form.instance)
        for product in form.cleaned_data['products']:      
            OrderProduct.objects.create(product=product, order=form.instance)
        return response

    def get_success_url(self) -> str: 
        return reverse_lazy('home')
