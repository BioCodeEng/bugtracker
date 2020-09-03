from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from bugtracker_app import forms
from bugtracker_app.forms import SignupForm
from bugtracker_app.models import CustomUser
# Create your views here.

@login_required
def index(request):
    return render(request, 'home.html', {'result': settings.AUTH_USER_MODEL})

def signup_view(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            signup_user = CustomUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                age=data.get('age')
            )
            if signup_user:
                return HttpResponseRedirect(reverse("login_page"))

    form = forms.SignupForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("home")))
    form = forms.LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
