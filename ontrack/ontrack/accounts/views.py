from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/accounts/login')
    template_name = 'signup.html'


class Dashboard(TemplateView):
	template_name = 'dashboard.html'
