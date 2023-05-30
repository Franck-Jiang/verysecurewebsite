from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from secureapp.models import Patient
from .forms import AppointmentForm, LoginForm, DoctorRegisterForm, RecordForm
from .models import Doctor, Record
from django.utils import timezone

# Create your views here.
def sign_up_doctor(request):
    if request.method == 'GET':
        form = DoctorRegisterForm()
        return render(request, 'registerd.html', { 'form': form})  
    
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            doctor = Doctor.objects.create(
                first_name  = form.cleaned_data['first_name'],
                last_name   = form.cleaned_data['last_name'],
                email       = form.cleaned_data['email'],
                speciality  = form.cleaned_data['speciality']
            )
            user.save()
            messages.success(request, 'You have singed up successfully as doctor.')
            login(request, user)
            return redirect('successD')
        else:
            return render(request, 'registerd.html', {'form': form})      

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
                return redirect('successd')           #redirection à changer
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'logind.html', {'form': form})

def success(request):
    return render(request, 'successd.html', {})

def base_view(request):
    # Logique de la vue
    context = {
        'message': 'Bonjour depuis la vue ABC !',
    }
    return render(request, 'baseD.html', context)

@login_required
def show_information(request):
    return None

@login_required
def add_record(request):
    if request.method == 'GET':
        form = RecordForm(initial={
            'doctor_email' : request.user.email
        })
        return render(request, 'record.html', { 'form': form})      
    
    if request.method == 'POST':
        form = RecordForm(request.POST)
        
        if form.is_valid():
            patient_email = form.cleaned_data['patient_email']
            doctor_email = form.cleaned_data['doctor_email']
            if Patient.objects.filter(email = patient_email).exists() and Doctor.objects.filter(email=doctor_email).exists():
                Record.objects.create(
                    title = form.cleaned_data['title'],
                    content = form.cleaned_data['content'],
                    patient_email = patient_email,
                    doctor_email = doctor_email,
                    date = timezone.now())
                return redirect('successD')
            else:
                messages.error(request, "Wrong emails provided")
                return  render(request, 'record.html', {'form': form})      

def delete_record(request):
    print("record deleted")
    return None