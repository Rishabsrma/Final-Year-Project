from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
# from django.contrib.auth.models import User
from multiple_users.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Profile, Doctor, Patient, Appointment



class MyPasswordChangeForm(PasswordChangeForm):
    oldpassword = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    newpassword1 = forms.CharField(label=_("New Password"), strip=False, widget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}),
    help_text = password_validation.password_validators_help_text_html())
    newpassword2 = forms.CharField(label=_("New Password Confirmation"), strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):    
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    help_text=password_validation. 
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email = forms.CharField(required= True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio'] 


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['Name', 'Phone_Num', 'Special']
        widgets = {'Name':forms.TextInput(attrs={'class':'form-control'}),'Phone_Num':forms.NumberInput(attrs={'class':'form-control'}), 'Special':forms.TextInput(attrs={'class':'form-control'})}        
               
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Name', 'Gender','Phone_Num', 'Address']
        widgets = {'Name':forms.TextInput(attrs={'class':'form-control'}), 'Gender':forms.TextInput(attrs={'class':'form-control'}),'Phone_Num':forms.NumberInput(attrs={'class':'form-control'}), 'Address':forms.TextInput(attrs={'class':'form-control'})}

class AppointmentProfileForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Doctor', 'Patient','Date', 'Time']
        widgets = {'Doctor':forms.Select(attrs={'class':'form-control'}) , 'Patient':forms.Select(attrs={'class':'form-control'}),'Date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}), 'Time':forms.TimeInput(attrs={'class':'form-control', 'type':'time'})}
