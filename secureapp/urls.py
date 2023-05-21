
from django.urls import path
from .views import login_view, register_view, abc_view



urlpatterns = [
    path('login/', login_view, name="Login"),
    path('register/', register_view, name="Register"),
    path('', abc_view)
]
