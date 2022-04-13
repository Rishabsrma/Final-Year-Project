from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from hospital_system.models import Contact
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


def doctor(request):
    return render(request,'profile.html')


def patient(request):
    return render(request,'profile.html')

class FaqView(TemplateView):
    model = Contact
    template_name = 'faq.html'    