from django.forms import ModelForm
from core.models import Order
from core.mixins.form_handler_mixin import FormHandlerMixin
from crispy_forms.layout import Submit, Layout, Div, Field


class OrderForm(FormHandlerMixin, ModelForm):
    class Meta:
        model = Order
        fields = ['pizzas','products','observation']

    def build_layout(self):
         return Layout(
             Div(
                 Div(Field('pizzas'), css_class='col-lg-12'),
                 css_class='row'
             ),
             Div(
                 Div(Field('products'), css_class='col-lg-12'),
                 css_class='row'
             ),
             Div(
                 Div(Field('observation'), css_class='col-lg-12')
                 , css_class='row'
             ),       
             Div(
                 Div(Submit('', 'CONCLUIR PEDIDO', css_class='btn btn-primary w-100 mt-5 button-form',css_id="btn-create-order"), css_class='col-lg-12'),
                 css_class='row justify-content-between mb-5')
        )