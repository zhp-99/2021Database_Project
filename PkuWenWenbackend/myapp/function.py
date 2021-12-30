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
from datetime import date, datetime, timedelta

def patient_info(userName):
    print('searching patient_info for ', userName)
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

def doctor_info(userName):
    obj = models.Doctor.objects.filter(userName=userName)
    res = {'retCode': -1, 'message': ''}
    if obj.count() == 0:
        res['retCode'] = 0
        res['message'] = '用户不存在'
        print('用户不存在')
    else:
        obj = models.Doctor.objects.get(userName=userName)

        res['retCode'] = 1
        res['message'] = '查询成功'
        res['realName'] = obj.realName
        res['doctorID'] = obj.id
        res['birthday'] = obj.birthday
        res['gender'] = obj.gender
        res['idCardNumber'] = obj.idCardNumber
        res['phoneNumber'] = obj.phoneNumber
        res['email'] = obj.email
        res['userName'] = obj.userName
        res['college'] = obj.college
        res['degree'] = obj.degree
        # res['FieldName'] = obj.FieldName
        # res['Specialty'] = obj.Specialty
        res['office'] = obj.office
        ke_zhang_dict = model_to_dict(models.Doctor.objects.get(office=obj.office, is_leader=True))
        res['officeLeaderName'] = ke_zhang_dict['realName']
        res['LeaderphoneNumber'] = ke_zhang_dict['phoneNumber']

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


def get_office_fever():
    retdata = {}
    office = model_to_dict(models.Office.objects.get(name='发热门诊'))
    doctor_num = len(models.Office.objects.raw('SELECT * FROM myapp_doctor WHERE office = %s', [office['name']]))
    res_list = list()
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


def today_appointment_list(userName):
    """
    :param userName: string
    :return: res = {'AppointmentList': appointment_list}
    """
    appointment_list = list()
    today = date.today()
    appointments = models.Appointment.objects.filter(dName=userName, date=today)
    for appointment in appointments:
        app_dic = model_to_dict(appointment)
        app_dic['date'] = str(app_dic['date'])
        app_dic['pRealName'] = models.Patient.objects.get(userName=app_dic['pName']).realName
        appointment_list.append(app_dic)
    res = {'AppointmentList': appointment_list}
    return res


def history_patient_list(userName):
    """
    :param userName: string
    :return: res = {'patient_list': patient_list}
    """
    patient_list = list()
    unique_list = list() # 仅仅为了确保不要插入重复的患者名，我拙劣的python技巧导致我这么写了
    appointments = models.Appointment.objects.filter(dName=userName)
    for appointment in appointments:
        app_dic = model_to_dict(appointment)
        pName = app_dic['pName']
        if pName not in unique_list:
            unique_list.append(pName)
            patient_list.append({'pName': pName, 'pRealName': models.Patient.objects.get(userName=pName).realName})
    res = {'PatientList': patient_list}
    return res



def doctor_appointments_by_date(request):
    userName = request.POST.get('userName')
    date = request.POST.get('date')
    app_list = models.Appointment.objects.filter(dName=userName,date=date)
    res_list = []
    for app in app_list:
        app_dict = model_to_dict(app)
        dName = app.dName
        pName = app.pName
        app_dict['dRealName'] = models.Doctor.objects.get(userName=dName).realName
        app_dict['pRealName'] = models.Patient.objects.get(userName=pName).realName
        res_list.append(app_dict)
    res = {'retCode': 1}
    res['appList'] = res_list
    return JsonResponse(res)


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


def prescription_info(pid):
    prescription = models.Prescription.objects.filter(id=pid)
    p_dict = model_to_dict(prescription[0])
    arr = list()
    arr.append(p_dict)
    res = {'prescription': arr}
    return res
    # [{'id': 1,
    #  'pName': 'Dee_Why',
    #  'dName': '张大夫',
    #  'date': datetime.date(2021, 12, 28),
    #  'medical': '牛黄解毒片'}]

