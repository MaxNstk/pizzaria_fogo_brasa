from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from core.api.v1.custom_router import CustomRouter
from core.views.home_view import HomeView
from django.contrib.auth.decorators import login_required
from core.views.order.order_create_view import OrderCreateView
from core.views.pizza.pizza_create_view import PizzaCreateView
from core.views.pizza.pizza_update_view import PizzaUpdateView
from core.views.pizza.pizza_list_view import PizzaListView

from core.views.register_view import RegisterView
from core.views.size.size_create_view import SizeCreateView
from core.views.size.size_list_view import SizeListView
from core.views.size.size_update_view import SizeUpdateView
from core.views.flavor.flavor_list_view import FlavorListView
from core.views.flavor.flavor_create_view import FlavorCreateView
from core.views.flavor.flavor_update_view import FlavorUpdateView
from core.views.product.product_list_view import ProductListView
from core.views.product.product_create_view import ProductCreateView
from core.views.product.product_update_view import ProductUpdateView
from core.views.customer.customer_list_view import CustomerListView
from core.views.order.order_list_view import OrderListView

router = CustomRouter()
urlpatterns = [ 
    # api urls
    path('api/v1/', include(router.urls)),

    # public views
    path('register/', RegisterView.as_view(), name='user_register'),
    path('', login_required(HomeView.as_view()), name='home'),
    
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/success/',
         PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>/',
         PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # login required views 

    path('', login_required(HomeView.as_view()), name='home'),
    path('size_create', login_required(SizeCreateView.as_view()), name='size_create'),
    path('size_list', login_required(SizeListView.as_view()), name='size_list'),
    path('size_update/<int:pk>', login_required(SizeUpdateView.as_view()), name='size_update'),

    path('flavor_list', login_required(FlavorListView.as_view()), name='flavor_list'),
    path('flavor_create', login_required(FlavorCreateView.as_view()), name='flavor_create'),
    path('flavor_update/<int:pk>', login_required(FlavorUpdateView.as_view()), name='flavor_update'),

    path('product_list', login_required(ProductListView.as_view()), name='product_list'),
    path('product_create', login_required(ProductCreateView.as_view()), name='product_create'),
    path('product_update/<int:pk>', login_required(ProductUpdateView.as_view()), name='product_update'),

    path('customer_list', login_required(CustomerListView.as_view()), name='customer_list'),

    path('pizza_list', login_required(PizzaListView.as_view()), name='pizza_list'),
    path('pizza_create', login_required(PizzaCreateView.as_view()), name='pizza_create'),
    path('pizza_update/<int:pk>', login_required(PizzaUpdateView.as_view()), name='pizza_update'),
    
    path('order_create', login_required(OrderCreateView.as_view()), name='order_create'),
    path('order_list', login_required(OrderListView.as_view()), name='order_list'),

]
