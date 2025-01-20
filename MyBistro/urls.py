from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from . import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('home_app.urls')),
    path('menu/', include('menu_app.urls')),
    path('location/', include('location_app.urls')),
    path('gallery/', include('gallery_app.urls')),
    path('order/', include('order_app.urls')),
    path('login/', include('login_accounts.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
    
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # to be able to upload images
