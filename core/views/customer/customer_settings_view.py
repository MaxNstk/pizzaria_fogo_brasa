
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.forms.user_form import UserForm

from core.models.user import User

class CustomerSettingsView(UpdateView):
    model = User
    form_class = UserForm
    template_name= 'customer_settings.html'

    def get_success_url(self):
        if not self.success_url:
            return reverse_lazy('login')
        else:
            return self.success_url 
