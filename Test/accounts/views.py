from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
from .forms import CreateUserForm


# Create your views here.
def LoginView(request):
    if request.user.is_authenticated:
        return redirect('dafitnessapp:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dafitnessapp:index')
            else:
                messages.info(request, 'Username or Password is incorrect')
        return render(request, 'accounts/login.html', {})


def SignUpView(request):
    if request.user.is_authenticated:
        return redirect('dafitnessapp:index')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was successfully created!')
                return redirect('accounts:login')
        else:
            form = CreateUserForm()
        return render(request, 'accounts/signup.html', {'form': form})


def LogOutView(request):
    logout(request)
    return redirect('accounts:login')
