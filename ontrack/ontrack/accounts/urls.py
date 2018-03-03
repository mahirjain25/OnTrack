from django.urls import path, include

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('',include('django.contrib.auth.urls')),
]