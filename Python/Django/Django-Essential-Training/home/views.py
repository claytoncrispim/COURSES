from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required # (replaced for LoginRequiredixin)
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'    


# Class based view: SignupView
class SignupView(FormView):
    template_name = 'home/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FarewellView(TemplateView):
    template_name = 'home/farewell.html'


# Class based views: HomeView and AuthorizedView
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url='/admin'

# Function based view
# def home(request):
#     # return HttpResponse('Hello, world!') # 1st way to return a response
#     return render(request, 'home/welcome.html', {'today': datetime.today()}) # 2nd way to return a response

# @login_required(login_url='/admin')
# def authorized(request):
#     return(render(request, 'home/authorized.html', {}))

# For learning notes:
# In this example, we have two views: HomeView (a class-based view) and authorized (a function-based view). The HomeView uses the TemplateView to render a template with some extra context, while the authorized view requires the user to be logged in and renders a different template.
# We replaced the function-based view for the home page with a class-based view, which is more concise and easier to maintain. The authorized view remains a function-based view to demonstrate the use of the login_required decorator.
