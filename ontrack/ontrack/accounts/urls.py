from django.urls import path, include

from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('signup/', views.SignUp.as_view(),name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('',include('django.contrib.auth.urls')),
    #path('', views.reminder, name = 'reminders'),
	path('new_reminder/',views.new_reminder, name = 'new_reminder'),
	path('edit_reminder/<pk>/',views.edit_reminder, name = 'edit_reminder'),
	path('delete_reminder/<pk>/',views.delete_reminder, name = 'delete_reminder'),
	path('new_book/',views.new_reminder, name = 'new_book'),
]
