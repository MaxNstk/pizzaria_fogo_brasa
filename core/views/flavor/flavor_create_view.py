from core.forms.flavor_form import FlavorForm
from core.views.generic.generic_create_view import GenericCreateView
from django.urls import reverse_lazy

class FlavorCreateView(GenericCreateView):
    form_class = FlavorForm
    template_name = 'generic_form.html'
