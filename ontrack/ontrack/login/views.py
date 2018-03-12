from django.shortcuts import render_to_response
#from django.shortcuts import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from . import forms
import json, pdb

def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
    return render(request, 'registration/login.html')

def signup_user(request):
    if request.POST:
        form = forms.MyRegistrationForm()
        form.username = request.POST.get('username')
        form.password1 = request.POST.get('password1')
        form.password2 = request.POST.get('password2')
        form.email = request.POST.get('email')
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'signup.html')