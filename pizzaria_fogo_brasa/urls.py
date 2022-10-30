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
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from core.views.home_view import HomeView
from core.views.admin_view import AdminView
from django.contrib.auth.decorators import login_required

from core.views.register_view import RegisterView

urlpatterns = [

    # public views
    path('register/', RegisterView.as_view(), name='user_register'),
    path('', login_required(HomeView.as_view()), name='home'),
    path('adm/', login_required(AdminView.as_view()), name='admin'),
    
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
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
]
