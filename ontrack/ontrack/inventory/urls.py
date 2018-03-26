from django.urls import path,include
from . import views

urlpatterns = [
path('inventory/',views.InventoryView,name='inventory'),
path('add_clothes',views.add_clothes,name='add_clothes'),
path('edit_cloth/<pk>/',views.edit_clothes, name = 'edit_cloth'),
path('delete_cloth/<pk>/',views.delete_clothes, name = 'delete_cloth'),
path('user_feedback/', views.new_feedback, name='feedback'),
path('add_fitness/', views.add_fitness, name='add_fitness'),
path('fitness/', views.fitness_view, name='fitness'),

]
