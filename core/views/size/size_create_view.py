from core.forms.size_form import SizeForm
from core.views.generic.generic_create_view import GenericCreateView

class SizeCreateView(GenericCreateView):

    form_class = SizeForm
    template_name = 'generic_form.html'
