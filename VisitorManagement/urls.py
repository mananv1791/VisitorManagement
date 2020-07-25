from django.urls import path
from templates import Main
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('message/<PhoneNumber>/', views.Message, name='message'),
    path('Customer/', views.Customer, name='Customer'),
    path('Manager/', views.manager, name='Manager'),
]
