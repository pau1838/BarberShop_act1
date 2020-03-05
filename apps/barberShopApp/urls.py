from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [

    path('<int:barberia_id>/', views.detail, name='detail'),
    path('', views.index, name= 'index'),
    path('<int:pk>/', views.barbers_list, name='barbers_list'),
    path('userprofile/', views.test, name='test')

]