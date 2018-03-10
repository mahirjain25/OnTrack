from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import render_to_response
import requests

import pyowm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/accounts/login')
    template_name = 'signup.html'


class Dashboard(generic.CreateView):
	
	template_name = 'dashboard.html'
	#render(request, template_name, {"temp" : temperature, "desc":desc})

	def get(self, request, *args, **kwargs):
		g = GeoIP2()
		ip = None#request.META.get('REMOTE_ADDR', None)
		if ip:
			latlong = g.lat_lon(ip) #function to obtain user's latitude and longitude
		else:
			latlong = [12.9141,74.8560] #coordinates of Mangalore
		owm  = pyowm.OWM('770a092b84f101cdc6b67b1c0976b341')
		obs = owm.weather_at_coords(latlong[0],latlong[1])
		w = obs.get_weather()
		desc = w.get_detailed_status()
		temperature = w.get_temperature(unit='celsius')['temp']
		context = locals()
		context['temp'] = temperature
		context['desc'] = desc
		return render(request, 'dashboard.html', {'desc' :desc, 'temp':temperature})

