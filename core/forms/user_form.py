from django.contrib.auth.forms import UserCreationForm
from core.mixins.form_handler_mixin import FormHandlerMixin
from crispy_forms.layout import Submit, Layout, Div, Field

from core.models.user import User

class UserForm(FormHandlerMixin, UserCreationForm):

    class Meta:
        model= User
        fields = ("first_name", "last_name",'phone_number')
    
    def build_layout(self):
        return Layout(
            Div(
                Div(Field('first_name'), css_class='col-lg-6'),
                Div(Field('last_name'), css_class='col-lg-6'),
                css_class='row'
            ),
            Div(
                Div(Field('phone_number'), css_class='col-lg-12')
                , css_class='row'
            ),      
            Div(
                Div(Submit('', 'Confirmar', css_class='btn w-100', css_id="btn-create-account"), css_class='col-lg-6'),
                css_class='row justify-content-center mb-5')
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False