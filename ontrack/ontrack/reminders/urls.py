from django.urls import path
from . import views


urlpatterns = [
		path('', views.reminder, name = 'reminders'),
		path('new/',views.new_reminder, name = 'new_reminder'),
]