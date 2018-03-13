from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . import forms

def homePageView(request):
	template_name = "base.html"


	 
	if request.POST.get('submit') == 'sign_in':
		username = request.POST['username']
		password = request.POST['password']
		print(username, password)
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('dashboard')

	elif request.POST.get('submit') == 'sign_up':
		form2 = forms.SignUpForm(request.POST)
		if form2.is_valid():
			form2.save()
			username = form2.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = username, password = raw_password)
			login(request, user)
			return redirect('dashboard')
	form1 = AuthenticationForm()
	form2 = forms.SignUpForm()

	return render(request, template_name, {'form1': form1, 'form2':form2})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

class AboutPageView(TemplateView):
	template_name = "about.html"


