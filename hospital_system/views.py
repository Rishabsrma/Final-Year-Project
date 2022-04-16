from importlib.metadata import files
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm
from django.views import View
from django.contrib import messages
from .models import Doctor, Contact, Patient 
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from .forms import DoctorProfileForm, PatientProfileForm, AppointmentProfileForm
from hospital_system.models import Doctor, User
from django.contrib.auth.decorators import login_required


# Create your views here.

def About(request):
    return render(request, 'about.html')


def Home(request):
    return render(request, 'index.html')  


def Navbar(request):
    return render(request, 'navbar.html')    


def AdminDashboard(request):
    return render(request, 'admin-dashboard.html') 

def AdminPage(request):
    return render(request, 'admin_page.html')     

# def Contact(request):
#     if request.method == 'POST':
#         names = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         content = request.POST.get('content')
#         print(names, email, phone, content)
#         contact = Contact(name=names,email=email, phone=phone, content=content)
#         contact.save()
#     return render(request, 'contact.html')     

@login_required
def Contact_view(request):
    if request.method == "POST":
        print(request.user)
        name = request.user
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        print(name,phone,email,content)
        
        if len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly!!!")
        else:    
            contact = Contact(Name = name,Phone = phone,Email = email,Content = content )
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'contact.html')

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)  
#         if form.is_valid():
#             user=form.get_user()
#             login(request, user)
#             if'next'in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:

#                 return redirect('login_admin')     
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login_admin.html', {'form':form})  

@login_required
def Services(request):
    return render(request, 'services.html')    


      
@login_required
def Profile(request):
    return render(request, 'profile.html')    


@login_required
def UpdateProfile(request):
    # profile = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
          
    context = {
         'u_form': u_form,
         'p_form': p_form
 }
    return render(request, 'update_profile.html', context)   


@login_required
def View_Doctor(request):
    if not request.user.is_admin:
        return redirect('login_view')
    doc = Doctor.objects.all()   
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)

@login_required
def Delete_Doctor(request, pid):
    if not request.user.is_admin:
        return redirect('login_view')
    doctor = Doctor.objects.get(id=pid) 
    doctor.delete()  
    return redirect('view_doctor')

@login_required
def Update_Doctor(request, pid):
    if not request.user.is_admin:
        return redirect('login_view')
    doctor = Doctor.objects.get(id=pid) 
    # doctor.update()  
    form = DoctorProfileForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('view_doctor')

    return render(request,'add_doctor.html',{'form':form})   

@login_required
def Update_Patient(request, pid):
    if not request.user.is_admin:
        return redirect('login_view')
    patient = Patient.objects.get(id=pid) 
    # patient.update()  
    form = PatientProfileForm(instance=patient)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('view_patient')

    return render(request,'add_patient.html',{'form':form})  

@login_required
def Update_Appointment(request, pid):
    if not request.user.is_admin:
        return redirect('login_view')
    appointment = Appointment.objects.get(id=pid)  
    form = AppointmentProfileForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentProfileForm(request.POST,instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('view_appointment')

    return render(request,'add_appointment.html',{'form':form})     


class Add_Doctor(View):
    def get(self, request):    

        form = DoctorProfileForm()
        # error = ""
        # if not request.user.is_admin:
        #     return redirect('login_view')
        # if request.method == 'POST':
        #     n = request.POST['name']
        #     c = request.POST['phone']
        #     sp = request.POST['special']
        #     try:
        #         Doctor.objects.create(Name=n, Phone_Num=c, Special=sp)
        #         error = 'no'
        #     except:
        #         error = 'yes'

        # d = {'error': error}
        return render(request, 'add_doctor.html', {'form': form}) 

    def post(self, request):
        form = DoctorProfileForm(request.POST)#data fetched from Doctorprofileform
        if form.is_valid():#checking form valid or not
            Name = form.cleaned_data['Name']
            Phone_Num = form.cleaned_data['Phone_Num']
            Special = form.cleaned_data['Special']
            reg = Doctor(Name=Name,Phone_Num=Phone_Num,Special=Special)
            reg.save()
            # messages.success(request, 'Added Successfully')
            return redirect('view_doctor')
        return render(request,'add_doctor.html',{'form':form})      

# class CustomerRegistrationView(View):
#     def get(self, request):
#         form = CustomerRegistrationForms()
#         return render(request,'signup.html',{'forms':form})

#     def post(self,request):
#         form = CustomerRegistrationForms(request.POST)
#         if form.is_valid():
#             messages.success(request,'You have been succesfully registered!')
#             form.save()
#         return render(request,'signup.html',{'forms':form}) 

# def search_Bar(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query:
#             searched = Doctor.objects.filter(Name__icontains=query)
#             return render(request,'searchbar.html', {'searched':searched})
#         else:
#             print("No information to show")
#             return request(request, 'searchbar.html', {})  
 
def search_Bar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = User.objects.filter(username__contains = searched)
        return render(request, 'searchbar.html', {'searched':searched,'results':results})
    else:
        return render(request, 'searchbar.html')

def View_Patient(request):
    if not request.user.is_admin:
        return redirect('login_view')
    doc = Patient.objects.all()   
    d = {'doc': doc}
    return render(request, 'view_patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_admin:
        return redirect('login_view')
    patient = Patient.objects.get(id=pid) 
    patient.delete()  
    return redirect('view_patient')

class Add_Patient(View):
    def get(self, request):
        form = PatientProfileForm()
 
        return render(request, 'add_patient.html', {'form': form}) 

    def post(self, request):
        form = PatientProfileForm(request.POST)#data fetched from Patientprofileform
        if form.is_valid():#checking form valid or not
            Name = form.cleaned_data['Name']
            Gender = form.cleaned_data['Gender']
            Phone_Num = form.cleaned_data['Phone_Num']
            Address = form.cleaned_data['Address']
            reg = Patient(Name=Name,Gender=Gender,Phone_Num=Phone_Num,Address=Address)
            reg.save()
            # messages.success(request, 'Added Successfully')
            return redirect('view_patient')
        return render(request,'add_patient.html',{'form':form})


class Add_Appointment(View): 
    def get(self, request):
        form = AppointmentProfileForm()

        return render(request, 'add_appointment.html', {'form': form})

    def post(self, request):
        form = AppointmentProfileForm(request.POST)#data fetched from Appointmentprofileform
        if form.is_valid():#checking form valid or not
            Doctor = form.cleaned_data['Doctor']
            Patient = form.cleaned_data['Patient']
            Date = form.cleaned_data['Date']
            Time = form.cleaned_data['Time']
            reg = Appointment(Doctor=Doctor,Patient=Patient,Date=Date,Time=Time)
            reg.save()
            # messages.success(request, 'Added Successfully')
            return redirect('view_appointment')
        return render(request,'add_appointment.html',{'form':form})  

def View_Appointment(request):
    if not request.user.is_admin:
        return redirect('login_view')
    doc = Appointment.objects.all()   
    d = {'doc': doc}
    return render(request, 'view_appointment.html', d)

def Delete_Appointment(request, pid):
    if not request.user.is_admin:
        return redirect('login_view')
    app = Appointment.objects.get(id=pid) 
    app.delete()  
    return redirect('view_appointment')         
 

# def update_data(request, id):
#     return render(request, 'view_patient.html',)
