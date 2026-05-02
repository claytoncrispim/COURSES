from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    # return HttpResponse('Hello, world!') # 1st way to return a response
    return render(request, 'home/welcome.html', {'today': datetime.today()}) # 2nd way to return a response