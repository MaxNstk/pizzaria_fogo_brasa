from core.forms.pizza_form import PizzaForm
from core.models.pizza import Pizza
from core.views.generic.generic_update_view import GenericUpdateView

class PizzaUpdateView(GenericUpdateView):
    model = Pizza
    form_class = PizzaForm
    template_name = 'generic_form.html'
