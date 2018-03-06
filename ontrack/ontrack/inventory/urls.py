from django.urls import path
from . import views

urlpatterns = [path('',views.InventoryView.as_view(),name = 'inventory')]
