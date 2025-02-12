from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from login_accounts.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()
 #ACTUALIZEAZA CU UN SINGUR BUTON
@login_required
def profile_view(request):
    user = User.objects.get(id=request.user.id)  
    
    if request.method == 'POST':
        user.email = request.POST.get('email', user.email)
        user.phone = request.POST.get('phone', user.phone)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        
        user.save()
        messages.success(request, "Profil actualizat cu succes!")
        return redirect('profile')  

    return render(request, 'profile.html', {'user': user})
