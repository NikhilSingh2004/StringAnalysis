from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'), # The Home Page that handles both GET & POST requests!.
]
