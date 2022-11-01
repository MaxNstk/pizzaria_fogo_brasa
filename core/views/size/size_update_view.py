from core.forms.size_form import SizeForm
from core.models.size import Size
from core.views.generic.generic_update_view import GenericUpdateView

class SizeUpdateView(GenericUpdateView):
    model = Size
    form_class = SizeForm
    template_name = 'generic_form.html'
