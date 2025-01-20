from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.login_signup_view),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    ]