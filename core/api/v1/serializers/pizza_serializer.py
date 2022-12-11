from rest_framework.serializers import ModelSerializer
from core.models import Pizza

class PizzaSerializer(ModelSerializer):

    class Meta:
        model= Pizza
        fields= '__all__'

    