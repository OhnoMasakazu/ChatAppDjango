from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

User = get_user_model()

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
        help_texts = {
            'username': None,
            'email': None,
        }