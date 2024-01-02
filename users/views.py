from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'login'
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