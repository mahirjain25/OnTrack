from django.urls import path

from . import views

urlpatterns = [
	path('', views.homePageView,name = 'home'),
	#path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
	path('about', views.AboutPageView.as_view(),name = 'about'),
	
]