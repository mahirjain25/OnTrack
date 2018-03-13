from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from inventory.forms import *
# Create your views here.


def InventoryView(request):
	template_name = 'inventory.html'
	return render(request,template_name)
	
	
	
	
def add_clothes(request):
	if request.method == 'POST': 
		form = AddClothesForm(request.POST)
		
		if form.is_valid():
			 return HttpResponseRedirect('')	#Need to redirect somewhere useful, for now if valid, then homepage
			
			
		
		
		
	else:
		form = AddClothesForm()	#Create a blank form
		
		
	return render(request,'inventory.html',{'form':form})
