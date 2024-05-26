from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class UserDispatchMixin():

    def dispatch(self, request, *args, **kwargs):
        response = super(UserDispatchMixin, self).dispatch(request, *args, **kwargs)
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('home'))
        return response


        