from django.urls import path

from . import views

urlpatterns = [
    # api directly for frontend-mounted
    path('patient/homepage/info', views.patient_homepage_info),
    path('office/info', views.office_info),
    path('reservation/calendar', views.reservation_calendar_info),
    path('patient/makeAppointment', views.make_appointment),
    path('medical/record/detail/info', views.medical_record_detail_info),
    path('doctor/homepage/info', views.doctor_homepage_info),
    path('appointment/detail/info', views.appointment_detail_info),
    # 真正有用的url绑定都在本行上面
    # 下面是鹏哥一开始盲写的内容，用于参考
    # zhp api
    path('doctor/register',views.docter_register),
    path('doctor/info', views.doctor_info),
    path('doctor/appointments',views.doctor_appointments),
    path('doctor/appointments/byDate',views.doctor_appointments_by_date),
    path('doctor/makeMR',views.make_mr),
    path('doctor/modify',views.modify_doctor),

    path('patient/register', views.patient_register),
    path('patient/info',views.patient_info),
    path('patient/modify',views.modify_patient),

    path('patient/appointments', views.patient_appointments),
    path('patient/appointments/byDate', views.patient_appointments_by_date),
    path('patient/mrs',views.patient_mrs),
    path('patient/mrs/byDate',views.patient_mrs_by_date),

    path('office/register',views.office_register),

    # old api
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