from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from inventory.forms import *
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
		form = AddClothesForm(request.POST)
		
		try:
			if form.is_valid():
				form.save()
				return redirect('inventory')
		except Exception as e:
			return HttpResponse("Cloth was not saved due to {}", e )
	else:
		form = AddClothesForm(instance = cloth)
	return render(request, template ,{"form":form ,"cloth": cloth})


@login_required(redirect_field_name='login')
def delete_clothes(request, pk):
	query = get_object_or_404(Clothes, pk =  pk)
	query.delete()
	
	return redirect('inventory')