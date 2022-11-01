from django.views.generic import CreateView

class GenericCreateView(CreateView):

    def get_success_url(self) -> str:
        return super().get_success_url()
