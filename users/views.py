from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, вы вошли в аккаунт")
                
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
                
    else:
        form = UserLoginForm()

    context = {"title": "login", "form": form}
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
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
            messages.success(request, f"{user.username}, вы вошли в аккаунт")

            # Redirect to the login page
            return HttpResponseRedirect(reverse("main:index"))
        else:
            # Debugging: Print form errors
            print(form.errors)
    else:
        form = UserRegistrationForm()

    context = {"title": "registration", "form": form}
    return render(request, "users/registration.html", context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Вы вышли из аккаунта")
    return redirect(reverse("users:login"))


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, f"Вы успешно обновили свой профиль")
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            # Debugging: Print form errors
            print(form.errors)
    else:
        form = ProfileForm(instance=request.user)

    context = {"title": "profile", "form": form}
    return render(request, "users/profile.html", context)
