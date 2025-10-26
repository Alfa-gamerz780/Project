"""
URL configuration for College project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('gallery/', views.gallery),
    path('eBook/', views.eBook),
    path('loginn/', views.loginn),
    path('signupp/', views.signupp),
    path('contactcode/', views.contactcode),
    path('signcode/', views.signcode),
    path('logincode/', views.logincode),
    path('dashboard/', views.dashboard),
    path('admin_login/', views.admin_login),
    path('admin_logincode/', views.admin_logincode),
]
