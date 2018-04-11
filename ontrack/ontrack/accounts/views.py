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
from django.contrib import messages
import pickle
import random
import datetime

quotes = {'Jimi Hendrix' : "When the power of love overcomes the love of power, the world will know peace.", 'Robert Frost': "The only way round is through." , 'Robert Frost': "By working faithfully eight hours a day you may eventually get to be boss and work twelve hours a day.", 'Denise Brennan-Nelson': "Someday is not a day of the week.", 'Robert Schuller': "Tough times never last, but tough people do.", 'Jamie Paolinetti': "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless.", 'Karen Lamb' :"A year from now you may wish you had started today.", 'Lao Tzu': "The journey of a thousand miles begins with one step."}

def SignUp(request):
    if request.method == "POST":
        form = forms.CustomSignUp
        template_name = 'base.html'
        if form.is_valid():
           	post = form.save(commit=False)
           	post.save()
           	messages.success(request, 'Signed Up Successfully')
           	return redirect(request,'login')
    else:
        form = forms.CustomSignUp
        return render(request, 'signup', {'form':form})

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
	author = random.choice(list(quotes))
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	quote = quotes[author]
	now = datetime.datetime.now()
	year = now.year
	month = now.month
	month = months[month-1]
	day = now.day
	minute= now.minute
	hour = now.hour
	if hour>12:
		hour = hour - 12
	rem_len = len(reminders)
	book_len = len(books)

	#quote, author = wikiquote.quote_of_the_day()
	return render(request, template_name, {"no_books": book_len,"no_reminders":rem_len, "reminders": reminders, "temp": temperature, "desc": desc, "imag": imag, "books":books, "quote": quote, "author": author, "year":year, "month":month, "day":day, "minute":minute ,"hour":hour})
	
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
def edit_book(request, pk):
	
	template = 'new_book.html'
	book = get_object_or_404(Book, pk = pk)
	
	if request.method == 'POST':
		book.delete()
		form = BookForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.user = request.user
			post.save()
			return redirect('dashboard')	
	else:
		form = BookForm(instance = book)
	return render(request, template ,{"form":form ,"book": book})

@login_required(redirect_field_name='login')
def delete_book(request, pk):
	query = get_object_or_404(Book, pk =  pk)
	query.delete()
	
	return redirect('/accounts/dashboard')
	
@login_required(redirect_field_name='login')
def user_profile(request):
	return render(request, 'user_profile.html')



@login_required(redirect_field_name='login')
def edit_user_profile(request, pk):
	template = 'edit_user_profile.html'
	reminder = get_object_or_404(User, pk = pk)
	
	if request.method == 'POST':
		form = CustomSignUp(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
		
	else:
		form = CustomSignUp(instance = request.user)
	return render(request, template ,{"form":form,"reminder":reminder})



@login_required(redirect_field_name='login')
def enter_subjects(request):
	template = 'enter_subjects.html'
	if request.method == "POST":
		form = TimetableForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False) 
			post.user = request.user
			post.save()
			return redirect('timetable')
	else:
		form = TimetableForm()
	return render(request,template,{"form":form})

@login_required(redirect_field_name='login')
def timetable(request):
	timetable = Timetable.objects.all()
	template_name = 'timetable.html'
	return render(request, template_name,{'timetable': timetable})
