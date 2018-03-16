from django.urls import path,include
from . import views

urlpatterns = [
path('inventory/',views.InventoryView,name='inventory'),
path('add_clothes',views.add_clothes,name='add_clothes'),
]
