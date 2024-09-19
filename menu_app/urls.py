from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('location/', include('location_app.urls')),
    path('gallery/', include('gallery_app.urls')),
   
]
