"""
URL configuration for riss_main project.

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
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index),
    path('reg',views.reg,name='reg'),
    path('login',views.login,name='login'),
    path('products',views.products,name='products'),
    path('home_css',views.home_css,name='home_css'),
    path('admin',views.admin,name='admin'),
    path('user_dashboard',views.user_dashboard,name='user_dashboard'),
    path('view_products',views.view_products,name="view_products"),
    path('product_update/<id>',views.product_update,name="product_update"),
    path('pd_delete/<id>',views.pd_delete,name="pd_delete"),
]
