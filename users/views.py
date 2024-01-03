from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

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
                return HttpResponseRedirect(reverse('main:index'))    
    else:
        form = UserLoginForm()


    context = {
        'title': 'login',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Debugging: Print cleaned_data to check form data
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            
            # Save the form data
            form.save()

            # Debugging: Print a message to check if this point is reached
            print("Form saved successfully")

            user = form.instance
            auth.login(request, user)

            # Redirect to the login page
            return HttpResponseRedirect(reverse('main:index'))
        else:
            # Debugging: Print form errors
            print(form.errors)
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'registration',
        'form': form
    }
    return render(request, 'users/registration.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))

def profile(request):
    context = {
        'title': 'profile'
    }
    return render(request, 'users/profile.html', context)