from rest_framework.viewsets import ModelViewSet
from core.api.v1.serializers.flavor_serializer import FlavorSerializer
from core.models.flavor import Flavor


class FlavorViewSet(ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer