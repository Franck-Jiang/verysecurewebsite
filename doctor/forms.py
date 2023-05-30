from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm      

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
       
class DoctorRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    speciality = forms.CharField(max_length=100)
    
    class Meta:
        model=User
        fields = ['email','password1','password2'] 
        
class AppointmentForm(forms.Form):
    patient_email = forms.EmailField(max_length=100)
    doctor_email = forms.EmailField(max_length=100)
    time = forms.TimeField()
    date = forms.DateField()
    place = forms.CharField()   
    
class RecordForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'cols': 50, 'rows': 20}))
    patient_email = forms.EmailField(max_length=100)
    doctor_email = forms.EmailField(max_length=100)
