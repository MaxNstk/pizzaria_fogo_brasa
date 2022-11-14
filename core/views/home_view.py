from django.views.generic.base import TemplateView
from core.forms.register_form import RegisterForm

class HomeView(TemplateView):

    customer_template = 'customer_home.html'
    admin_template = 'base_admin.html'

    def get_template_names(self):
        return [self.admin_template] if self.request.user.is_superuser else [self.customer_template]