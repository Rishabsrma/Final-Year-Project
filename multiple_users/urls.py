from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import FaqView

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    # path('doctor/', views.doctor, name='doctor'),
    # path('patient/', views.patient, name='patient'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_view'),name='logout'),
]