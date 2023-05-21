from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)   #form à personnaliser
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vue de redirection')           #redirection à changer
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def abc_view(request):
    # Logique de la vue
    context = {
        'message': 'Bonjour depuis la vue ABC !',
    }
    return render(request, 'abc.html', context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)   #form à personnaliser

        print(form['firstname'])
        if form.is_valid():
            [fname, lname, email, phone, age, zip] = [  form.cleaned_data['firstname'], 
                                                        form.cleaned_data['lastname'],
                                                        form.cleaned_data['email'],
                                                        form.cleaned_data['phone'],
                                                        form.cleaned_data['age'],
                                                        form.cleaned_data['zipcode']]
            print( [fname, lname, email, phone, age, zip])
            if form.cleaned_data['password'] == form.cleaned_data['confirmpass']:
                #add in db
                pass
            else :
                render(request, 'register.html', {'firstname': fname,
                                                'lastname': lname,
                                                'email': email,
                                                'phone': phone,
                                                'age': age,
                                                'zipcode': zip})
        else:
            #Not valid
            errors = form.errors 
            for err in errors:
                print(err)
            messages.error(request, (f"Not a valid form, got {errors}"))
            
            
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form' : form})