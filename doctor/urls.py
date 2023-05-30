
from django.urls import path
from .views import add_record, login_view, sign_out, success, base_view, show_information, sign_up_doctor



urlpatterns = [
    path('login/', login_view, name="LoginD"),
    path('logout/', sign_out, name="LogoutD"),
    path('register/', sign_up_doctor, name="RegisterD"),
    path('info/', show_information, name="InfoD"),
    path('success/', success, name="successD"),
    path('', base_view, name='doctor'),
    path('create_record/', add_record, name="create_record"),
]
