from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signUp/', views.singUp, name='signUp'),
    path('login/', views.login, name='login'),

    # url system
    path('addUser/', views.signUpForm, name='addUser'),
]