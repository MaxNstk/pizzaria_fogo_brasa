from rest_framework.routers import DefaultRouter
from core.api.v1.viewsets.order_viewset import OrderViewSet
from core.api.v1.viewsets.pizza_viewset import PizzaViewSet
from core.api.v1.viewsets.product_viewset import ProductViewSet

from core.api.v1.viewsets.user_modelviewset import UserViewSet
from core.api.v1.viewsets.flavor_modelviewset import FlavorViewSet
from core.api.v1.viewsets.size_modelviewset import SizeViewSet


class CustomRouter(DefaultRouter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register('user', UserViewSet)
        self.register('size', SizeViewSet)
        self.register('flavor', FlavorViewSet)
        self.register('product', ProductViewSet)
        self.register('pizza', PizzaViewSet)
        self.register('order', OrderViewSet)

        