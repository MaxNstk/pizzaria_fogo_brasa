from django.contrib.auth.views import LoginView as DjangoLoginView

class LoginView(DjangoLoginView):
    
    template_name = "login.html"