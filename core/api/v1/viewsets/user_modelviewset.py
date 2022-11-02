from rest_framework.viewsets import ModelViewSet
from core.api.v1.serializers.user_serializer import UserSerializer
from core.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer