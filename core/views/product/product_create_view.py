from core.forms.product_form import ProductForm
from core.views.generic.generic_create_view import GenericCreateView
from django.urls import reverse_lazy

class ProductCreateView(GenericCreateView):
    form_class = ProductForm
    template_name = 'generic_form.html'
