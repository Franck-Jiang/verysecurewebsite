from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"