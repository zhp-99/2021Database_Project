
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),

    path('doctor/register',views.docter_register),
    path('doctor/info', views.doctor_info),
    path('doctor/appointments',views.doctor_appointments),
    path('doctor/appointments/byDate',views.doctor_appointments_by_date),
    path('doctor/makeMR',views.make_mr),

    path('patient/register', views.patient_register),
    path('patient/info',views.patient_info),
    path('patient/modify',views.modify_patient),
    path('patient/makeAppointment',views.make_appointment),
    path('patient/appointments', views.patient_appointments),
    path('patient/appointments/byDate', views.patient_appointments_by_date),
    path('patient/mrs',views.patient_mrs),
    path('patient/mrs/byDate',views.patient_mrs_by_date)
    #path('patient/info',views.patient_info)
]