from core.forms.product_form import ProductForm
from core.models.product import Product
from core.views.generic.generic_update_view import GenericUpdateView

class ProductUpdateView(GenericUpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'generic_form.html'
