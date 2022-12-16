
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
            return reverse_lazy('home')
        else:
            return self.success_url 
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)