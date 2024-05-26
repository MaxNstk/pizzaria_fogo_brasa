from django.forms import ModelForm
from core.models import Pizza, Flavor, Size


class PizzaForm(ModelForm):

    class Meta:
        model = Pizza
        fields = ['flavor','size','price','is_active']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            return
        self.fields['flavor'].queryset = Flavor.objects.filter(is_active=True)
        self.fields['size'].queryset = Size.objects.filter(is_active=True)
        