from django.forms import ModelForm
from core.models.product import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['flavor','size','price','available']
