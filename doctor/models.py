from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Appointment(models.Model):
    patient_email = models.EmailField(max_length=100)
    doctor_email = models.EmailField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    place = models.TextField()
    
    def __str__(self):
        return f"{self.time} {self.patient_email.split('@')[0]} {self.doctor_email.split('@')[0]}"
    
class Record(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=10000)
    patient_email = models.EmailField(max_length=100)
    doctor_email = models.EmailField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.title}"
