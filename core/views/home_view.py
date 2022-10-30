from django.views.generic.base import TemplateView
from core.forms.register_form import RegisterForm
from core.models.user import User

class HomeView(TemplateView):

    customer_template = 'customer_home.html'
    admin_template = 'admin_home.html'

    def get_template_names(self):
        return [self.admin_template] if self.request.user.is_superuser else [self.customer_template]