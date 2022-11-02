from rest_framework.serializers import ModelSerializer
from core.models import Flavor

class FlavorSerializer(ModelSerializer):

    class Meta:
        model= Flavor
        fields= '__all__'

    