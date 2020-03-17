from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('barbershop/<int:pk>/', views.barbers_list, name='barbers_list'),
    path('barbershop/<int:pk_bs>/barber/<int:pk_b>/', views.barber_detail, name='barber_detail'),
    path('barbershop/<int:pk_bs>/barber/<int:pk_b>/cita/<int:pk_p>/', views.appointment_reserve, name='appointment_reserve'),
    path('barbershop/<int:pk_bs>/barber/<int:pk_b>/cita/<int:pk_p>/thanks', views.assign_appointment, name='assign_appointment'),
    path('register/',views.registration_view, name ="register"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logut')
]
