from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.ajax_login, name='login'),
    
]