from django.views.generic.edit import CreateView

from core.forms.size_form import SizeForm


class SizeCreateView(CreateView):

    form_class = SizeForm
    template_name = ''
    # fazer um tempalte padrão