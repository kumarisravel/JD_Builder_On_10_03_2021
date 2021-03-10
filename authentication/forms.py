from django.forms import ModelForm
from .models import PasswordTable
from django import forms
from django.forms import Form


class SignUpForm(Form):
    Email=forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'id':'password',
        'placeholder':'Enter Email Address'
        }
    ))

    Name=forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'id':'password',
        'placeholder':'Enter Full Name'
        }
    ))
    Password=forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'id': 'password',
        'placeholder':'Create Your  Password'
        }
    ))
    Retype_Password=forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'id': 'password',
        'placeholder':'Create Your  Password'
        }
    ))

