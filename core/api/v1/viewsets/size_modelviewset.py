from rest_framework.viewsets import ModelViewSet
from core.api.v1.serializers.size_serializer import SizeSerializer
from core.models import Size


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer