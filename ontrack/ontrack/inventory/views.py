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
