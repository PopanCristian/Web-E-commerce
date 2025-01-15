from django.shortcuts import render
from django.conf import settings

# Create your views here.
def location_view(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'location.html',context)