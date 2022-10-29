
from django.views.generic.edit import CreateView
from core.forms.register_form import RegisterForm

from core.models.user import User

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name= 'registration/register.html'

