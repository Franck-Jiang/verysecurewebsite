from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

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
    
    return render(request, 'login.html', {'form': form})

def success(request):
    return render(request, 'success.html', {})

def base_view(request):
    # Logique de la vue
    context = {
        'message': 'Bonjour depuis la vue ABC !',
    }
    return render(request, 'base.html', context)

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('success/')         #à changer
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form}) 
    
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
        return render(request,'login.html',{'form': form})

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', { 'form': form})  
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('success/')
        else:
            return render(request, 'register.html', {'form': form})
    
      
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('success/')  


def add_record(request):
    print("record added")
    return None

def delete_record(request):
    print("record deleted")
    return None

def consult_record(request):
    print("record consulted")
    return None

def upload_file(request):
    print("file uploaded")
    return None
