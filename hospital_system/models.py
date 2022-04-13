from tokenize import Name
from django.db import models
# from django.contrib.auth.models import User
from multiple_users.models import User

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from PIL import Image
from django.conf import settings

# Create your models here.

class Doctor(models.Model):
    Name = models.CharField(max_length=20)
    Phone_Num = models.IntegerField(null=True)
    Special = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.Name)

class Patient(models.Model):
    Name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Phone_Num = models.IntegerField(null=True)
    Address = models.TextField()

    def __str__(self):
        return  str(self.Name)
        
class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
        return  str(self.Doctor)

class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=13)
    Email = models.CharField(max_length=100)
    Content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.Name + ' - ' + self.Email 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics\default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="Hello.")

    def __str__(self):
        return f'{self.user.username} Profile'
        
    def save(self, ** kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 600:
            output_size = (350, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

