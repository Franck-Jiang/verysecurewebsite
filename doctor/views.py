from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm, DoctorRegisterForm
from .models import Doctor

# Create your views here.
def sign_up_doctor(request):
    if request.method == 'GET':
        form = DoctorRegisterForm()
        return render(request, 'registerd.html', { 'form': form})  
    
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.first_name.lower()+user.last_name.lower()
            doctor = Doctor.objects.create(
                first_name  = form.cleaned_data['first_name'],
                last_name   = form.cleaned_data['last_name'],
                email       = form.cleaned_data['email'],
                speciality  = form.cleaned_data['speciality']
            )
            user.save()
            messages.success(request, 'You have singed up successfully as doctor.')
            login(request, user)
            return redirect('success/')
        else:
            return render(request, 'registerd.html', {'form': form})      
        
def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('success/')         #à changer
        
        form = LoginForm()
        return render(request, 'logind.html', {'form': form}) 
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('abc/')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'logind.html',{'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return render(request, 'success.html', {})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)   #form à personnaliser
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success/')           #redirection à changer
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'logind.html', {'form': form})

def success(request):
    return render(request, 'success.html', {})

def base_view(request):
    # Logique de la vue
    context = {
        'message': 'Bonjour depuis la vue ABC !',
    }
    return render(request, 'baseD.html', context)

def show_information(request):
    return None