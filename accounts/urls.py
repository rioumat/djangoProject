from django.urls import path

from . import views

# Needs to be added into the main project urls.py file too
# those buttons are in the __navbar partial

urlpatterns = [
    path('login', views.login, name='login'), 
    path('register', views.register, name='register'), 
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]
