from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    zipcode = models.IntegerField()
    phone_num = models.CharField(max_length=100)
    
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    speciality = models.CharField(max_length=100)
    
    username =  models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    
    def __str__(self):
        return self.username