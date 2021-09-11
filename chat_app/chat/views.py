from chat.forms import SignupForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'chat/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request,'chat/signup.html',{'form': form})

def friend(request):
    return render(request,'chat/friend.html')


