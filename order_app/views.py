from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category


# Create your views here.
@login_required(login_url='/login/')
def orderNow_view(request):
    categories = Category.objects.all()  
    return render(request, 'order.html', {'categories': categories})