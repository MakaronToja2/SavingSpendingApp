"""
URL configuration for SavingSpendingApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Savings.views import savings_list, add_saving
from .views import home_view
from accounts.views import login_view

urlpatterns = [
    path("", home_view),
    path('admin/', admin.site.urls),
    path('savings/', savings_list, name='savings_list'),
    path('savings/add/', add_saving, name='add_saving'),
    path("login/", login_view, name='login_view'),
]
