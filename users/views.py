from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users import forms
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request);
    return HttpResponseRedirect('/user/login')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.type == 'PATIENT':
                return HttpResponseRedirect('/doctors/')
            elif user.type == 'DOCTOR':
                return HttpResponseRedirect('/doctors/appointments/')
            # else:
            #     return HttpResponseRedirect('/user/profile')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            print(username,raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
    else:
        form = forms.SignupForm()
    return render(request, 'signup.html', {'form': form})
