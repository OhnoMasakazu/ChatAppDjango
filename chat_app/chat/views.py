from chat.forms import SignupForm, MessageForm, UsernameChangeForm, MailChangeForm, IconChangeForm, PasswordChangeForm, User, TalkHistory
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import logging

# Create your views here.
def index(request):
    return render(request,'chat/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request,'chat/signup.html',{'form': form})

def friend(request):
    params = {
        'data': User.objects.all(),
        'user': request.user,
    }
    return render(request,'chat/friend.html',params)

def talk(request,friendname):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.username
            message.receiver = friendname
            message.save()
            return redirect('talk', friendname)
    else:
        form = MessageForm()
    params = {
        'friendname': friendname,
        'user': request.user,
        'form': form,
        'talkdata': TalkHistory.objects.all(),
    }
    return render(request,'chat/talk.html',params)

def setting(request):
    return render(request,'chat/setting.html')

def username_change(request):
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            user_obj = User.objects.get(username=request.user.username)
            user_obj.username = username
            user_obj.save()
            return redirect('username_done')
    else:
        form = UsernameChangeForm()
    return render(request,'chat/username_change.html',{'form': form})

def mail_change(request):
    if request.method == 'POST':
        form = MailChangeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            email_obj = User.objects.get(username=request.user.username)
            email_obj.email = email
            email_obj.save()
            return redirect('mail_done')
    else:
        form = MailChangeForm()
    return render(request,'chat/mail_change.html',{'form': form})

def icon_change(request):
    if request.method == 'POST':
        form = IconChangeForm(request.POST)
        if form.is_valid():
            icon = form.cleaned_data["icon"]
            icon_obj = User.objects.get(username=request.user.username)
            icon_obj.icon = icon
            icon_obj.save()
            return redirect('icon_done')
    else:
        form = IconChangeForm()
    return render(request,'chat/icon_change.html',{'form': form})

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            password_obj = User.objects.get(username=request.user.username)
            password_obj.password = password
            password_obj.save()
            return redirect('password_done')
    else:
        form = PasswordChangeForm()
    return render(request,'chat/password_change.html',{'form': form})

def username_done(request):
    return render(request,'chat/username_done.html')

def mail_done(request):
    return render(request,'chat/mail_done.html')

def icon_done(request):
    return render(request,'chat/icon_done.html')

def password_done(request):
    return render(request,'chat/password_done.html')
