from chat.forms import SignupForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import User

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
    data = User.objects.all()
    params = {
        'data': data,
    }
    return render(request,'chat/friend.html',params)

def talk(request):
    return render(request,'chat/talk.html')

def setting(request):
    return render(request,'chat/setting.html')