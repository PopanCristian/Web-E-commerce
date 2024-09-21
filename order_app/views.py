from django.shortcuts import render

# Create your views here.
def orderNow_view(request):
    return render(request,'orderNow.html')