from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from core.mixins.form_handler_mixin import FormHandlerMixin

from core.models.user import User

class RegisterForm(UserCreationForm, FormHandlerMixin):

    class Meta:
        model= User
        fields = ("first_name", "last_name", 'phone_number', 'cpf_cnpj', "username","password1", "password2")