from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, InformationForm, PatientRegisterForm
from .models import Patient


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
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('home')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})
        
def sign_up_patient(request):
    if request.method == 'GET':
        form = PatientRegisterForm()
        return render(request, 'register.html', { 'form': form})  
    
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            patient = Patient.objects.create(
                first_name  = form.cleaned_data['first_name'],
                last_name   = form.cleaned_data['last_name'],
                email       = form.cleaned_data['email'],
                age         = form.cleaned_data['age'],
                zipcode     = form.cleaned_data['zipcode'],
                phone_num   = form.cleaned_data['phone_num'],                
            )
            form.save()
            messages.success(request, 'You have singed up successfully as patient.')
            login(request, user)
            return redirect('success/')
        else:
            return render(request, 'register.html', {'form': form})        
          
def patient_information(request):
    if request.method == 'GET':
        patient = Patient.objects.get(email=request.user.username)
             
        form = InformationForm( initial={       
                                'first_name' : patient.first_name,
                                'last_name' : patient.last_name,
                                'email' : patient.email,
                                'age' : patient.age,
                                'zipcode' : patient.zipcode,
                                'phone_num' : patient.phone_num}  )

        return render(request, 'personal.html', {'form': form})      
    
    if request.method == 'POST':
        form = InformationForm()
        if form.is_valid():
            patient = Patient.objects.get(email=request.user.username)
            patient.first_name = form.cleaned_data['first_name']
            patient.last_name = form.cleaned_data['last_name']
            patient.age = form.cleaned_data['age']
            patient.zipcode = form.cleaned_data['zipcode']
            patient.phone_num = form.cleaned_data['phone_num']
            patient.save()
            return render(request, 'success.html', {})
        else:
            messages.error(request, f"Error")
            return render(request, 'personal.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('success/')  

def redirect_doctor(request):
    return redirect('/')  
    
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
