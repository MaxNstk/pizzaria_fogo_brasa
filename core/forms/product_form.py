from django.forms import ModelForm
from core.models.product import Product
from core.mixins.form_handler_mixin import FormHandlerMixin
from crispy_forms.layout import Submit, Layout, Div, Field


class ProductForm(FormHandlerMixin,ModelForm):
    class Meta:
        model = Product
        fields = ['description','price','available']

    def build_layout(self):
        return Layout(
            Div(
                Div(Field('description'), css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div(Field('price'), css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div(Field('available'), css_class='col-lg-12')
                , css_class='row'
            ),       
            Div(
                Div(Submit('', 'Gravar', css_class='btn btn-primary w-100 button-form'), css_class='col-lg-3'),
                css_class='row justify-content-between mb-5')
        )