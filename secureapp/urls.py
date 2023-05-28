
from django.urls import path
from .views import login_view, sign_out, success, base_view, sign_up



urlpatterns = [
    path('login/', login_view, name="Login"),
    path('login/success/', success, name="Login success"),
    path('logout/success/', success, name="Logout success"),
    path('register/success/', success, name="Register success"),
    path('logout/', sign_out, name="Logout"),
    path('register/', sign_up, name="Register"),
    path('', base_view)
]
