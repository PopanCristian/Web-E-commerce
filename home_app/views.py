from django.shortcuts import render
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # Afișează șablonul 'home.html'

# Create your views here.
