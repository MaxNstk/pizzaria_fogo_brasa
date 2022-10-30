from django.views.generic.base import TemplateView
from core.forms.register_form import RegisterForm

from core.models.user import User

class HomeView(TemplateView):
    template_name= 'base_home.html'

