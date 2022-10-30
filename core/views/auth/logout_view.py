from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse

class LogoutView(DjangoLogoutView):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return self.logout_then_login(request, next_page=reverse('login'))
