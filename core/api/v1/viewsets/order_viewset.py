from rest_framework.viewsets import ModelViewSet
from core.api.v1.serializers.order_serializer import OrderSerializer
from core.models.order import Order


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer