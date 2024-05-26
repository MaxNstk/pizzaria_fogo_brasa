from core.forms.flavor_form import FlavorForm
from core.models.flavor import Flavor
from core.views.generic.generic_update_view import GenericUpdateView

class FlavorUpdateView(GenericUpdateView):
    model = Flavor
    form_class = FlavorForm
    template_name = 'generic_form.html'
