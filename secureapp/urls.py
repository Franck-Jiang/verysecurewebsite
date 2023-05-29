
from django.urls import path
from .views import redirect_doctor, sign_in, sign_out, success, base_view, patient_information, sign_up_patient



urlpatterns = [
    path('login/', sign_in, name="Login"),
    path('login/success/', success, name="Login success"),
    path('logout/success/', success, name="Logout success"),
    path('register/success/', success, name="Register success"),
    path('logout/', sign_out, name="Logout"),
    path('register/', sign_up_patient, name="RegisterPatient"),
    path('info/', patient_information, name="Info"),
    path('success/', success, name="success"),
    path('', base_view, name='home')
]
