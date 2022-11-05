from django.forms import ModelForm
from core.models import Flavor
from core.mixins.form_handler_mixin import FormHandlerMixin
from crispy_forms.layout import Submit, Layout, Div, Field


class FlavorForm(FormHandlerMixin, ModelForm):
    class Meta:
        model = Flavor
        fields = ['name','description', 'is_active']

    def build_layout(self):
        return Layout(
            Div(
                Div(Field('name'), css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div(Field('description'), css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div(Field('is_active'), css_class='col-lg-12')
                , css_class='row'
            ),       
            Div(
                Div(Submit('', 'Gravar', css_class='btn btn-primary w-100 button-form'), css_class='col-lg-3'),
                css_class='row justify-content-between mb-5')
        )
