from core.forms.size_form import SizeForm
from core.views.generic.generic_create_view import GenericCreateView
from django.urls import reverse_lazy

class SizeCreateView(GenericCreateView):
    form_class = SizeForm
    template_name = 'generic_form.html'
