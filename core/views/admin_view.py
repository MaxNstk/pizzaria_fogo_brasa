from django.views.generic.base import TemplateView
from core.forms.register_form import RegisterForm

from core.models.user import User

class AdminView(TemplateView):
    template_name= 'admin_home.html'
