from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('register-user/', views.register_user, name='register_user'),
    path('register-car/', views.register_car, name='register_car'),
    path('cars/', views.car_list, name='car_list'),
    path('contact-history/', views.contact_history_list, name='contact_history_list'),
]
