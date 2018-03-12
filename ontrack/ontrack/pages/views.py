from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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
				return HttpResponseRedirect('accounts/dashboard')

	elif request.POST.get('submit') == 'sign_up':
		form2 = UserCreationForm(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('/')
	form1 = AuthenticationForm()
	form2 = UserCreationForm()

	return render(request, template_name, {'form1': form1, 'form2':form2})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

class AboutPageView(TemplateView):
	template_name = "about.html"


