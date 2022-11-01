"""pizzaria_fogo_brasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from core.views.home_view import HomeView
from django.contrib.auth.decorators import login_required

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

urlpatterns = [

    # public views
    path('register/', RegisterView.as_view(), name='user_register'),
    path('', login_required(HomeView.as_view()), name='home'),
    
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password_change/<str:model>/<int:pk>/', PasswordChangeView.as_view(),
    #      name='admin_password_change'),
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
]
