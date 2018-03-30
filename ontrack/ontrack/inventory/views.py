from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from django.shortcuts import redirect
import matplotlib.pyplot as plt
import numpy as np

from django.contrib.auth.decorators import login_required



@login_required(redirect_field_name='login')
def InventoryView(request):
	clothes = Clothes.objects.order_by('category')
	template_name = 'clothes.html'
	return render(request,template_name, {"clothes": clothes})
	
	
	
	
@login_required(redirect_field_name='login')
def add_clothes(request):
	if request.method == 'POST': 
		form = AddClothesForm(request.POST)
		
		if form.is_valid():
			new = form.save(commit = False)
			new.author = request.user
			new.save()
			return redirect('inventory')	#Need to redirect somewhere useful, for now if valid, then homepage
	else:
		
		form = AddClothesForm()	#Create a blank form
		
		
	return render(request,'new_cloth.html',{'form':form})

@login_required(redirect_field_name='login')
def edit_clothes(request, pk):
	
	template = 'new_cloth.html'
	cloth = get_object_or_404(Clothes, pk = pk)
	
	if request.method == 'POST':
		try:
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				return redirect('inventory')
		except Exception as e:
			return HttpResponse("Cloth was not saved due to {}".format(e) )
	else:
		form = AddClothesForm(instance = cloth)
	return render(request, template ,{"form":form ,"cloth": cloth})


@login_required(redirect_field_name='login')
def delete_clothes(request, pk):
	query = get_object_or_404(Clothes, pk =  pk)
	query.delete()
	return redirect('inventory')
	

@login_required(redirect_field_name='login')
def new_feedback(request):	
	
	if request.method == "POST":
		form = FeedbackForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.user = request.user
			post.save()
			return redirect('dashboard')
	else:
		form = FeedbackForm()
	return render(request, 'feedback.html', {'form': form})

@login_required(redirect_field_name='login')
def fitness_view(request):
	fit = Fitness.objects.order_by('category')
	date = []
	calorie = []
	

	for i in fit:
		if(i.user.username==User.username):
			continue
		date.append(i.created_date)
		calorie.append(i.calories)
	for i in range(len(date)):
		for j in range(i+1, len(date)):
			if(j>len(date)):
				break
			
			if(date[j].date() ==date[i].date()):
				
				calorie[i]+= calorie[j]
				del date[j]
				del calorie[j]
			if(j+1>len(date)):
				break
	date.pop(-1)
	calorie.pop(-1)
	date = np.array(date)
	calorie = np.array(calorie)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(date, calorie)

 # format your data to desired format. Here I chose YYYY-MM-DD but you can set it to whatever you want.
	import matplotlib.dates as mdates
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%h-%y'))

# rotate and align the tick labels so they look better
	fig.autofmt_xdate()
	plt.scatter(date, calorie)
	plt.title('Fitness Information')
	plt.xlabel('Date')
	plt.ylabel('Calories Burnt')
	plt.savefig("./accounts/test.png",bbox_inches='tight')
	plt.show()
	

	template_name = 'fitness.html'
	return render(request,template_name, {"fit": fit})

@login_required(redirect_field_name='login')
def add_fitness(request):
	MET = {
	"Run": 7.0,
	"Cycle Ride": 5.5, 
	"Jump Rope": 10.0,
	"Tennis" :6.8,
	"Football": 10.3, 
	"Swimming": 9.0,
	"Badminton": 5.5, 
	"Basketball": 11.1, 
	"Yoga": 3.2, 
	"Weight Lifting": 10.9,
	"Cricket":6.1,
	"CrossFit": 10.2
	}
	if request.method == "POST":
		form = AddFitnessForm(request.POST)
		if form.is_valid():
			## Logic for calculating calories
			post = form.save(commit = False)
			post.calories = MET[post.category] * post.weight * post.duration /60.0
			post.user = request.user
			post.save()
			return redirect('fitness')
	else:
		form = AddFitnessForm()
	return render(request, 'add_fitness.html', {'form': form})

