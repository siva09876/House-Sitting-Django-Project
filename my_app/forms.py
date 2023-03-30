from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model=MyUser
        fields=['first_name','last_name','username','email','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }