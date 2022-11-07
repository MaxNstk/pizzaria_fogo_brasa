from django.views.generic import CreateView
from django.urls import reverse_lazy

from core.mixins.dispatch_user_mixin import UserDispatchMixin


class GenericCreateView(UserDispatchMixin, CreateView):
    pass
