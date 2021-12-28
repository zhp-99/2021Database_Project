from django.urls import path

from . import views

urlpatterns = [
    path('doctor/register',views.docter_register),
    path('doctor/info', views.doctor_info),
    path('doctor/appointments',views.doctor_appointments),
    path('doctor/appointments/byDate',views.doctor_appointments_by_date),
    path('doctor/makeMR',views.make_mr),
    path('doctor/modify',views.modify_doctor),

    path('patient/register', views.patient_register),
    path('patient/info',views.patient_info),
    path('patient/modify',views.modify_patient),
    path('patient/makeAppointment',views.make_appointment),
    path('patient/appointments', views.patient_appointments),
    path('patient/appointments/byDate', views.patient_appointments_by_date),
    path('patient/mrs',views.patient_mrs),
    path('patient/mrs/byDate',views.patient_mrs_by_date),

    path('office/register',views.office_register),

    path('register', views.register),
    path('login', views.login),
    path('getOfficeIndex',views.getOfficeIndex),
    path('getCourseIndex',views.getCourseIndex),
    path('getQuestionIndex',views.getQuestionIndex),
    path('getAnswerList',views.getAnswerList),
    path('likeAnswer',views.likeAnswer),
    path('dislikeAnswer',views.dislikeAnswer),
    path('addQuestion',views.addQuestion),
    path('addReply',views.addReply),
    path('openSchool', views.openSchool),
    path('openCourse', views.openCourse),
    path('openQuestion', views.openQuestion),
    path('submitQuestion', views.submitQuestion),
]