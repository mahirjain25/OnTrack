from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from django.shortcuts import redirect

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
	clothes = Clothes.objects.order_by('category')
	template_name = 'fitness.html'
	return render(request,template_name, {"fit": fit})
	
@login_required(redirect_field_name='login')
def add_fitness(request):
	MET = {
	"Run": 7.0,
	"Cycle": 5.5, 
	"Jump Rope": 10.0,
	"Tennis" :6.8,
	"Football": 10.3, 
	"Swimming": 9.0,
	"Badminton": 5.5, 
	"Basketball": 11.1, 
	"Yoga": 3.2, 
	"Weightlifting": 10.9,
	"Cricket":6.1,
	"CrossFit": 10.2


	}
	if request.method == "POST":
		form = AddFitnessForm(request.POST)
		if form.is_valid():
			## Logic for calculating calories
			post = form.save(commit = False)
			post.calories = int(MET[post.category] * post.weight * post.duration /60.0)
			post.user = request.user
			post.save()
			return redirect('fitness')
	else:
		form = AddFitnessForm()
	return render(request, 'add_fitness.html', {'form': form})

