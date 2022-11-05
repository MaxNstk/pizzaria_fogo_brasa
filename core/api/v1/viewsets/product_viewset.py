from rest_framework.viewsets import ModelViewSet
from core.api.v1.serializers.product_serializer import ProductSerializer
from core.models.product import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer