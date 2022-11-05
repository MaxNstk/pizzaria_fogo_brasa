from django.contrib.auth.forms import UserCreationForm
from core.mixins.form_handler_mixin import FormHandlerMixin
from crispy_forms.layout import Submit, Layout, Div, Field

from core.models.user import User

class RegisterForm(FormHandlerMixin, UserCreationForm):

    class Meta:
        model= User
        fields = ("first_name", "last_name", 'phone_number', 'cpf_cnpj', "username","password1", "password2")
    
    def build_layout(self):
        return Layout(
            Div(
                Div(Field('first_name'), css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div(Field('last_name'), css_class='col-lg-12')
                , css_class='row'
            ),
            Div(
                Div(Field('phone_number'), css_class='col-lg-12')
                , css_class='row'
            ),
            Div(
                Div(Field('cpf_cnpj'), css_class='col-lg-12')
                , css_class='row'
            ), 
            Div(
                Div(Field('phone_number'), css_class='col-lg-12')
                , css_class='row'
            ), 
            Div(
                Div(Field('password1'), css_class='col-lg-12')
                , css_class='row'
            ),
            Div(
                Div(Field('password2'), css_class='col-lg-12')
                , css_class='row'
            ),        
            Div(
                Div(Submit('', 'Cadastrar-se', css_class='btn w-100', css_id="btn-create-account"), css_class='col-lg-6'),
                css_class='row justify-content-center mb-5')
        )