from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import FaqView, Patient_AppointmentView, ManageAppointmentView

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('patient-appointment/',Patient_AppointmentView.as_view(), name='patient-appointment'),
    path('manage-appointments/',ManageAppointmentView.as_view(), name='manage-appointments'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_view'),name='logout'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
]