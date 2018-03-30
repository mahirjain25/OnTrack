from django.urls import path, include

from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('signup/', views.SignUp.as_view(),name='signup'),
    #path('login/', views.Login.as_view(),name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('',include('django.contrib.auth.urls')),
    #path('clothes/', views.clothes, name='clothes'),
    #path('', views.reminder, name = 'reminders'),
	path('new_reminder/',views.new_reminder, name = 'new_reminder'),
	path('edit_reminder/<pk>/',views.edit_reminder, name = 'edit_reminder'),
	path('delete_reminder/<pk>/',views.delete_reminder, name = 'delete_reminder'),
	path('new_book/',views.new_book, name = 'new_book'),
    path('user_profile/',views.user_profile, name = 'user_profile'),
    path('edit_user_profile/<pk>/',views.edit_user_profile, name = 'edit_user_profile'),
    path('enter_subjects/',views.enter_subjects, name = 'enter_subjects'),
    path('timetable/',views.timetable, name = 'timetable'),

]
