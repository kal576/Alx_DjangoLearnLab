from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def register_view(request):
    """Django's inbuilt authenticatioin view"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

def home(request):
    return render(request, "blog/home.html")

def login_view(request):
    """Django's inbuilt login view"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirec("home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def profile_view(request):
    """
    Profile management
    View and edit profile details eg email
    """
    if request.methos == "POST":
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})
