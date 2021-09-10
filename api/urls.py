"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from core.views import RegisterView, LogView, EventView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token
from core import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('log/add/', LogView.as_view(), name='log'),
    path('log/all/', LogView.getAll, name='logall'),
    path('log/<str:user_email>/', LogView.getByUserEmail, name='logbyuseremail'),
    path('profile/<str:user_email>/', ProfileView.profile, name='profile'),
    path('edit-profile/<str:user_email>/', ProfileView.as_view(), name='profile'),
    path('events/', EventView.as_view(), name='events')
]