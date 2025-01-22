from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User



def login_signup_view(request):

    if request.method == 'POST':

        if 'login' in request.POST:

            username = request.POST['username_login']
            password = request.POST['password_login'] # get the credentials
            user = authenticate(request, username = username, password = password)

            if user is not None: # check if users does exist
                login(request, user)
                return redirect('/order/')
            else:
                messages.success(request, "Fa-ti cont băi nene ")

        elif 'signup' in request.POST:

            username = request.POST['username_signup']
            email = request.POST['email_signup']
            password = request.POST['password_signup']
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            login(request, user)
            return redirect('home')  # redirecționează după înregistrare
    
    return render(request, 'login&signup.html') # just send de login/sigup page

