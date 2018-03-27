from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.utils import timezone
#from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import render_to_response
import requests
from .forms import *
import pyowm
from django.shortcuts import redirect
from .models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from . import forms
import wikiquote
from django.contrib.auth.models import User
class SignUp(generic.CreateView):
    form_class = AuthenticationForm#forms.CustomSignUp
    success_url = reverse_lazy('login')
    template_name = 'base.html'

    def func(request):
    	return HttpResponseRedirect("/")
class Login(generic.CreateView):
	form_class = AuthenticationForm
	template_name = 'login.html'

@login_required(redirect_field_name='login')
def dashboard(request):
	reminders = Reminder.objects.filter(created_date__lte=timezone.now()).order_by('due_date')
	books = Book.objects.filter().order_by('date_of_return')
	#return render(request, 'reminder.html',{'reminders': reminders})
	template_name = 'dashboard.html'
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
	
	d = {"lightning":"https://i.imgur.com/99BrvGA.png", "thunder":"https://i.imgur.com/99BrvGA.png", "thunderstorm":"https://i.imgur.com/99BrvGA.png","sun": "https://i.imgur.com/J0heQg7.png", "clear":  "https://i.imgur.com/J0heQg7.png","day": "https://i.imgur.com/J0heQg7.png","drizzle" :"https://i.imgur.com/zFJAEWp.png","rain" :"https://i.imgur.com/zFJAEWp.png", "snow" : "https://i.imgur.com/vOSIvVb.png", "cloud" :"https://cdn2.iconfinder.com/data/icons/wthr/32/cloudy-512.png", "hot" : "https://i.imgur.com/bIcsdMF.png",}
	imag  = None
	for i in d:
		if i in desc:
			imag = d[i]
			break
	if temperature >= 33:
		imag = d["hot"]
	quote, author = wikiquote.quote_of_the_day()
	return render(request, template_name, {"reminders": reminders, "temp": temperature, "desc": desc, "imag": imag, "books":books, "quote": quote, "author": author})
	
@login_required(redirect_field_name='login')
def reminder(request):
	reminders = Reminder.objects.filter(created_date__lte=timezone.now()).order_by('due_date')
	return render(request, 'reminder.html',{'reminders': reminders})


@login_required(redirect_field_name='login')
def new_reminder(request):
	if request.method == "POST":
		form = ReminderForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.published_date = timezone.now()
			post.author = request.user
			post.save()
			return redirect('dashboard')
	else:
		form = ReminderForm()
	return render(request, 'new_reminder.html', {'form': form})

@login_required(redirect_field_name='login')
def edit_reminder(request, pk):
	
	template = 'new_reminder.html'
	reminder = get_object_or_404(Reminder, pk = pk)
	
	if request.method == 'POST':
		reminder.delete()
		form = ReminderForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
			return redirect('dashboard')	
	else:
		form = ReminderForm(instance = reminder)
	return render(request, template ,{"form":form ,"reminder": reminder})


@login_required(redirect_field_name='login')
def delete_reminder(request, pk):
	query = get_object_or_404(Reminder, pk =  pk)
	query.delete()
	
	return redirect('/accounts/dashboard')

@login_required(redirect_field_name='login')
def book(request):
	books = Book.objects.filter().order_by('date_of_return')
	return render(request, 'reminder.html',{'books': books, "new_reminder": url_name})
	
	
@login_required(redirect_field_name='login')
def new_book(request):
	template = 'new_book.html'
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.published_date = timezone.now()
			post.user = request.user
			post.save()
			return redirect('dashboard')
	else:
		form = BookForm()
	return render(request,template,{"form":form})
	
@login_required(redirect_field_name='login')
def user_profile(request):
	return render(request, 'user_profile.html')



@login_required(redirect_field_name='login')
def edit_user_profile(request, pk):
	template = 'edit_user_profile.html'
	reminder = get_object_or_404(User, pk = pk)
	
	if request.method == 'POST':
		form = CustomSignUp(request.POST)
		
		try:
			if form.is_valid():
				form.save()
				return redirect('dashboard')
		except Exception as e:
			return HttpResponse("Reminder was not saved due to {}", e )
	else:
		form = CustomSignUp(instance = reminder)
	return render(request, template ,{"form":form ,"reminder": reminder})
