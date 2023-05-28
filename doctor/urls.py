
from django.urls import path
from .views import login_view, sign_out, success, base_view, show_information, sign_up_doctor



urlpatterns = [
    path('login/', login_view, name="Login"),
    path('logout/', sign_out, name="Logout"),
    path('register/', sign_up_doctor, name="RegisterPatient"),
    path('info/', show_information, name="Info"),
    path('success/', success, name="success"),
    path('', base_view)
]
