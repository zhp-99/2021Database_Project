from django.forms import model_to_dict
from django.shortcuts import render
from . import models
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.tokens import default_token_generator
import json
import requests
import json
from django.core.mail import send_mail
from django.conf import settings
import re
import random
import json
import dateutil.parser

def patient_info(userName):
    obj = models.Patient.objects.filter(userName=userName)
    res = {'retCode': -1, 'message': ''}
    if obj.count() == 0:
        res['retCode'] = 0
        res['message'] = '用户不存在'
        print('用户不存在')
    else:
        obj = models.Patient.objects.get(userName=userName)

        res['retCode'] = 1
        res['message'] = '查询成功'
        res['userName'] = obj.userName
        res['patientID'] = obj.id
        res['realName'] = obj.realName
        res['gender'] = obj.gender
        res['idCardNumber'] = obj.idCardNumber
        res['birthday'] = obj.birthday
        res['phoneNumber'] = obj.phoneNumber
        res['email'] = obj.email
        print('查询成功')
    return res


def patient_appointment_count(userName):
    app_list = models.Appointment.objects.filter(pName=userName)
    res = {'appointmentNumber': len(app_list)}
    return res


def get_office_index():
    retdata = {}
    offices = models.Office.objects.values()
    office_list = list(offices)
    res_list = list()
    for office in office_list:
        doctor_num = len(models.Office.objects.raw('SELECT * FROM myapp_doctor WHERE office = %s', [office['name']]))
        res_list.append({'office_name': office['name'], 'doctor_num': doctor_num})
    retdata['OfficeList'] = res_list
    return retdata


def get_doctor_index(office):
    doctor_list = models.Doctor.objects.filter(office=office)
    res_list = []
    for doc in doctor_list:
        doc_dict = model_to_dict(doc)
        res_list.append(doc_dict)
    res = {'DoctorList': res_list}
    return res


def patient_appointments(userName):
    app_list = models.Appointment.objects.filter(pName=userName)
    res_list = []
    for app in app_list:
        app_dict = model_to_dict(app)
        dName = app.dName
        pName = app.pName
        app_dict['dRealName'] = models.Doctor.objects.get(userName=dName).realName
        app_dict['pRealName'] = models.Patient.objects.get(userName=pName).realName
        app_dict['date'] = str(app_dict['date'])
        res_list.append(app_dict)
    res = {'retCode': 1, 'AppointmentList': res_list}
    return res


def appointments_by_doctor_date(userName, date):
    app_list = models.Appointment.objects.filter(dName=userName,date=date)
    res_list = []
    for app in app_list:
        app_dict = model_to_dict(app)
        dName = app.dName
        pName = app.pName
        app_dict['dRealName'] = models.Doctor.objects.get(userName=dName).realName
        app_dict['pRealName'] = models.Patient.objects.get(userName=pName).realName
        res_list.append(app_dict)
    return res_list


def patient_medical_records(userName):
    mr_list = models.MedicalRecord.objects.filter(pName=userName)
    res_list = []
    for mr in mr_list:
        mr_dict = model_to_dict(mr)
        dName = mr.dName
        pName = mr.pName
        mr_dict['dRealName'] = models.Doctor.objects.get(userName=dName).realName
        mr_dict['pRealName'] = models.Patient.objects.get(userName=pName).realName
        mr_dict['date'] = str(mr_dict['date'])
        res_list.append(mr_dict)
    res = {'MedicalRecordList': res_list}
    return res

