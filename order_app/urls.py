from django.urls import path
from . import views


urlpatterns=[
  path('', views.orderNow_view, name='order'),
  path('<str:category_name>/', views.category_products, name='category_products')
  
]