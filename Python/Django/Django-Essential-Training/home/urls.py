from unicodedata import name

from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), # replaced views.home for views.HomeView class that uses the 'as_view' method . Unlike the instructor's code, I added the forward slash "/" after "home" to avoid 404 error. It seems that without it, the URL pattern doesn't match and results in a 404 error when trying to access http://   
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('farewell/', views.FarewellView.as_view(), name='farewell'),
]

# For learning notes:
# After changing home/views.py from a function based view to a class based one, using TemplateView, I tried to access http://127.0.0.1:8000/home/ it was returning 404 error. I found that I hadn't put the forward slash "/" in path('home'), so it should be path('home/'). It worked after it. One important thing to mention is that before that change - views.home to views.HomeView.as_view() - the page was working correctly
# The video screenshot at 'Django-Essential-Training/screenshots/Screenshot from 2026-05-05 13-13-26.png' shows the instructor's code, which still misses that forward slash in path('home', ...), reinforcing that it didn't use to have it before the change, but for the instructor's there was no 404 error.
# Model: when reading this information for the learning notes of class 04, try to explain why it happens and what is the best way to avoid it.
# OBS: The very same thing happened with the authorized end point. Without the "/" after "authorized", it will run into 404 error.