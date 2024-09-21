from django.urls import path
from . import views


urlpatterns=[
  path('',views.orderNow_view, name='order')
]