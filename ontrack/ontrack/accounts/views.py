from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
url = api_address + 'Mangalore'
json_data = requests.get(url).json()
lol = "hey"

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/accounts/login')
    template_name = 'signup.html'


class Dashboard(TemplateView):
	template_name = 'dashboard.html'
	weather = lol

