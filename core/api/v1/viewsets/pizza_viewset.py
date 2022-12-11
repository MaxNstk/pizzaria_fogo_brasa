from rest_framework.viewsets import ModelViewSet
from core.api.v1.serializers.pizza_serializer import PizzaSerializer
from core.models.pizza import Pizza


class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer