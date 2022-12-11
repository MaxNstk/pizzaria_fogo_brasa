from django.views.generic import CreateView
from core.forms.order_form import OrderForm

class OrderCreateView(CreateView):

    template_name = 'order_form.html'
    form_class = OrderForm
