from django.views.generic.base import TemplateView
from core.forms.register_form import RegisterForm
from core.models.user import User

class HomeView(TemplateView):

    customer_template = 'customer_home.html'
    admin_template = 'admin_home.html'

    def get(self, request, *args, **kwargs):
        self.template = self.admin_template if request.user.is_superuser else self.customer_template
        super().get(self, request, *args, **kwargs)
