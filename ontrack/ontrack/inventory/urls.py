from django.urls import path,include
from . import views

urlpatterns = [
path('inventory/',views.InventoryView,name='inventory'),
path('',include('django.contrib.auth.urls')),]
