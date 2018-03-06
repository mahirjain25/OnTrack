from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


class InventoryView(TemplateView):
	template_name = 'inventory.html'
