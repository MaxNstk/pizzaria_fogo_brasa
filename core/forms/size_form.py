from django.forms import ModelForm
from core.models.size import Size
from core.mixins.form_handler_mixin import FormHandlerMixin
from crispy_forms.layout import Submit, Layout, Div, Field

class SizeForm(FormHandlerMixin, ModelForm):
    class Meta:
        model=Size
        fields=['short_name', 'description','available']
    
    def build_layout(self):
        return Layout(
            Div(
                Div(Field('short_name'), css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div(Field('description'), css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div(Field('available'), css_class='col-lg-12')
                , css_class='row'
            ),
            Div(
                Div(Field('password2'), css_class='col-lg-12')
                , css_class='row'
            ),        
            Div(
                Div(Submit('', 'Gravar', css_class='btn btn-primary w-100'), css_class='col-lg-3'),
                css_class='row justify-content-between mb-5')
        )