"""
URL configuration for smartnotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home), # This is the old way of doing it. It is now handle by the home app's urls.py file.

    path('', include('home.urls')), # This is the new way of doing it. It tells Django to look for a urls.py file in the home app and use it to handle any URLs that start with '' (which is the root URL).

    path('smart/', include('notes.urls')), # This tells Django to look for a urls.py file in the notes app and use it to handle any URLs that start with 'smart/'.
]
