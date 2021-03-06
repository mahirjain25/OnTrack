from django.shortcuts import render_to_response
#from django.shortcuts import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.views import generic
from . import forms
import json, pdb

def login_user(request):
    error = ""
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
        else:
            error= "Invalid user name and password combination"
    return render(request, 'login.html', {"error": error})


class SignUp(generic.CreateView):
    form_class = forms.MyRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

