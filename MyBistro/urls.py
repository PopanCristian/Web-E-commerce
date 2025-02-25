from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from . import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('', include('home_app.urls')),
    path('menu/', include('menu_app.urls')),
    path('location/', include('location_app.urls')),
    path('gallery/', include('gallery_app.urls')),
    path('order/', include('order_app.urls')),
    path('login/', include('login_accounts.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/',include ('user_profile.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls)
    
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # to be able to upload images
