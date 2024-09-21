from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.location_view, name='location'),
    
   
]
