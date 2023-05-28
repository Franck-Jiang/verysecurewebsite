from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm      

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
      
      
class PatientRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    age = forms.IntegerField()
    zipcode = forms.IntegerField()
    phone_num = forms.CharField(max_length=100)
    
    class Meta:
        model=User
        fields = ['email','password1','password2'] 
class InformationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    age = forms.IntegerField()
    zipcode = forms.IntegerField()
    phone_num = forms.CharField(max_length=100)