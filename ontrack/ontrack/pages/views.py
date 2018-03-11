from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class homePageView(TemplateView):
	template_name = "base.html"
	

class AboutPageView(TemplateView):
	template_name = "about.html"
