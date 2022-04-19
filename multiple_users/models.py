from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)

class Patient_Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    DOCTOR_CHOICES = (
        ('Pediatrician', 'Pediatrician'),
        ('Cardiologist', 'Cardiologist'),
        ('Oncologist', 'Oncologist'),
        ('Gastroenterologist', 'Gastroenterologist'),
        ('Pulmonologist', 'Pulmonologist'),
        ('Nephrologist', 'Nephrologist'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Otolaryngologist', 'Otolaryngologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Neurologist', 'Neurologist'),
        ('Radiologist', 'Radiologist'),
        ('Anesthesiologist', 'Anesthesiologist'),
        ('Surgeon', 'Surgeon'),
    )
    Department = models.CharField(max_length=50,choices=DOCTOR_CHOICES, null=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]
