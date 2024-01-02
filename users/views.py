from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm

# Create your views here.
def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))    
    else:
        form = UserLoginForm()


    context = {
        'title': 'login',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'registration'
    }
    return render(request, 'users/registration.html', context)

def logout(request):
    context = {
        'title': 'logout'
    }
    return render(request, 'users/login.html', context)

def profile(request):
    context = {
        'title': 'profile'
    }
    return render(request, 'users/profile.html', context)