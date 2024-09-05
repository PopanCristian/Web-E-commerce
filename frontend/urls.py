from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rută care mapază către funcția index din views.py
]
