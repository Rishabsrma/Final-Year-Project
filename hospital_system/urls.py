from django.urls import path
from hospital_system.views import About,Home,Navbar,Services,Doctors,Contact_view,Profile,UpdateProfile,AdminDashboard,AdminPage,View_Doctor,Delete_Doctor,Delete_Patient,Add_Doctor,View_Patient,Add_Patient,Add_Appointment,Delete_Appointment,View_Appointment
from . import views
from django.contrib.auth import views as auth_views
from .forms import  MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', Home,name='home'),
    path('about/', About,name='about'),
    path('navbar/', Navbar,name='navbar'),
    path('contact/', Contact_view,name='contact'),
    path('services/', Services,name='services'),
    path('doctors/', Doctors,name='doctors'),
    path('profile/', Profile,name='profile'),
    path('update_profile/', UpdateProfile,name='update_profile'),
    path('admin-dashboard/', AdminDashboard,name='admin-dashboard'),
    path('admin-page/', AdminPage,name='admin-page'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', views.Add_Doctor.as_view(), name='add_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('add_patient/', views.Add_Patient.as_view(), name='add_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_appointment/', views.Add_Appointment.as_view(), name='add_appointment'),
    path('delete_doctor(?P<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('delete_patient(?P<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('update_doctor(?P<int:pid>)/', views.Update_Doctor, name='update_doctor'),
    path('update_patient(?P<int:pid>)/', views.Update_Patient, name='update_patient'),
    path('delete_appointment(?P<int:pid>)/', Delete_Appointment, name='delete_appointment'),
    path('update_appointment(?P<int:pid>)/', views.Update_Appointment, name='update_appointment'),
    path('search/', views.search_Bar,name='search'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form = LoginForm), name='login'),
    # path('accounts/login/admin', auth_views.LoginView.as_view(template_name='login_admin.html', authentication_form = LoginForm), name='login_admin'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html', success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # path('registration/', views.CustomerRegistrationView.as_view(),name='register'),


    
]
