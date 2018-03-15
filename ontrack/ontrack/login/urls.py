from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_user),
    path('signup/', views.SignUp.as_view(),
]
