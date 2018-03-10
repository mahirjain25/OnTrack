from django.urls import path, include

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('',include('django.contrib.auth.urls')),
]
