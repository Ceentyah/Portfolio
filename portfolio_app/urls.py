from django.urls import path
from . import views  # Import your views from the current directory

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home page
]
