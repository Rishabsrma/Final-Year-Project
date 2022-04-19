from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from hospital_system.models import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect
from multiple_users.models import Patient_Appointment
from django.views.generic import ListView
import datetime
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string, get_template
# Create your views here.


def signup(request):
    return render(request, 'signup.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('home')
            else:
                msg= 'Please enter your credentials correctly!!!'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin-dashboard.html')


class Patient_AppointmentView(TemplateView):
    def get(self,request):
        pp = Patient_Appointment.objects.values_list('Department').all()
        
        ppsort = sorted(list(set([a.strip() for lang in pp for a in lang])))
        print(ppsort)
        return render(request,'patient_appointment.html',{'ppsort':ppsort})
    
    
    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('request')
        department = request.POST.get('special')

        appointment = Patient_Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            Department=department,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment. We will reach out to you ASAP!!!")
        return HttpResponseRedirect(request.path)

class FaqView(TemplateView):
    model = Contact
    template_name = 'faq.html'   

class ManageAppointmentView(ListView):
    template_name = 'manage-appointments.html' 
    model = Patient_Appointment
    context_object_name = 'appointments'
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get('date')
        appointment_id = request.POST.get('appointment-id')
        appointment = Patient_Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()


        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)    
        appointments = Patient_Appointment.objects.all()
        context.update({
            "title":"Manage Appointments"          
        })
        return context

# def Appointment_view(request):
#     context = {}
#     context['form'] = Patient_Appointent()
#     return render( request, "patient-appointment.html", context)