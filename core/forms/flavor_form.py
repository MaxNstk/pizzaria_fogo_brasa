

from django.forms import ModelForm
from core.models import Flavor


class FlavorForm(ModelForm):
    class Meta:
        model = Flavor
        fields = ['name','description', 'available']
