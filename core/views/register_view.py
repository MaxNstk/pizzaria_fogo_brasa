
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.forms.register_form import RegisterForm

from core.models.user import User

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name= 'generic_form.html'


    def get_success_url(self):
        if not self.success_url:
            return reverse_lazy('login')
        else:
            return self.success_url 