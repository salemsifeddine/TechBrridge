from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.db.models.base import Model
from django.forms import ModelForm, fields, widgets
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *
username_validator = UnicodeUsernameValidator()





class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'placeholder': 'username',"name":"username"}))
    password = forms.CharField(max_length=63,  widget=forms.PasswordInput(attrs={'placeholder': 'Password',"name":"password"}))
    
    class Meta:
        model=User
        fields = ["username","password"]