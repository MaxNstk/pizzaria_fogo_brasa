from rest_framework.serializers import ModelSerializer
from core.models import Size

class SizeSerializer(ModelSerializer):

    class Meta:
        model= Size
        fields= '__all__'

    