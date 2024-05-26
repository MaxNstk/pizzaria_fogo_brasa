from django.forms import ModelForm
from core.models.address import Address


class AddressForm(ModelForm):

    class Meta:
        model = Address
        fields = ['customer','address','number','district','zip_code','note']
    