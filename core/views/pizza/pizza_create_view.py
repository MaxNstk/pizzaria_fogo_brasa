from core.forms.pizza_form import PizzaForm
from core.views.generic.generic_create_view import GenericCreateView
from django.urls import reverse_lazy

class PizzaCreateView(GenericCreateView):
    form_class = PizzaForm
    template_name = 'generic_form.html'
