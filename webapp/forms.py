from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Asset
from .models import Employee
from django.conf.urls.static import static

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=35, widget=forms.PasswordInput)

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ('asset_owner', 'asset_name', 'asset_desc')

        labels = {
            'asset_owner' : 'Asset Owner',
            'asset_name' : '',
            'asset_desc' : '',
        }

        widgets = {
            'asset_owner': forms.Select(attrs={'class':'form-control', 'placeholder':'Asset Owner'}),
            'asset_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset Name'}),
            'asset_desc': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Asset Description'}),
        }

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('full_name', 'date_of_birth', 'address')

        labels = {
            'full_name' : '',
            'date_of_birth' : '',
            'address' : '',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),
            'date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Birth (MM/DD/YYYY)'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
        }