from django.contrib import admin
from .models import Appointment, Doctor, Record

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Record)
admin.site.register(Appointment)