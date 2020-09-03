#went through this in auth demo refer to Login and SignupForm there
# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm): #SignupForm
    class Meta:
        model = CustomUser
        fields = ["displayname"]
    username = forms.CharField(max_length=130)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form): #LoginForm
    username = forms.CharField(max_length=130)
    password = forms.CharField(widget=forms.PasswordInput)
