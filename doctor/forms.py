from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm      

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
       
class DoctorRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    speciality = forms.CharField(max_length=100)
    
    class Meta:
        model=User
        fields = ['email','password1','password2'] 