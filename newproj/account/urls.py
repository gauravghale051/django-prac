
from django.urls import path
from .views import *

urlpatterns = [
    path('ho', home,name="name"),
    path('about', about,name="about"),
   
]