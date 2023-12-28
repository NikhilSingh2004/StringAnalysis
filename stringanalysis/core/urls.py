from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('<int:count>/', views.Home, name='home'),
    path('<str:reverse>/', views.Home, name='home'),
    path('<int:words>', views.Home, name='home'),
]
