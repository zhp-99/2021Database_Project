
from django.urls import path

from . import views

urlpatterns = [
    path('patient/register', views.patient_register),
    path('doctor/register',views.docter_register),
    path('login',views.login),
    path('patient/info',views.patient_info),
    path('doctor/info',views.doctor_info)
    #path('patient/info',views.patient_info)
]