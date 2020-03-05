from django.contrib import admin
from django.urls import path
from apps.barberShopApp import views

urlpatterns = [
    path('<int:pk>/', views.barbers_list, name='barbers_list'),
    path('userprofile/', views.test, name='test')
    path('<int:barberia_id>/', views.detail, name='detail'),
    path('', views.index, name= 'index')
]