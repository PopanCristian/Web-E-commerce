from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Ruta pentru pagina principală
    path('menu/', include('menu_app.urls')),
]
