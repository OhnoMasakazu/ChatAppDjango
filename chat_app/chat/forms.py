from django import forms
from django.contrib.auth import get_user_model
from .models import User,TalkHistory
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()
#forms.ModelForm
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2','icon',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = TalkHistory
        fields = ('text',)

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ("username",)

class MailChangeForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ("email",)

class IconChangeForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ("icon",)

class PasswordChangeForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ('password',)