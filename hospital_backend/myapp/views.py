from django.shortcuts import render

# Create your views here.
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

@csrf_exempt
def patient_register(request):
    userName = request.POST.get('userName', 'username')
    password = request.POST.get('password', 'xxx')
    email = request.POST.get('email', '未注册')

    realName = request.POST.get('realName','xxx')
    phoneNumber = request.POST.get('phoneNumber','xxx')
    idCardNumber = request.POST.get('idCardNumber','xxx')
    gender = request.POST.get('gender','x')
    birthday = dateutil.parser.parse(request.POST.get('birthday','2000-01-01'))



    res = {'retCode': 0, 'message': ''}

    obj = models.Patient.objects.filter(userName=userName)
    if obj.count() == 0:

        models.Patient.objects.create(
            userName=userName, password=password,email=email,realName=realName,
            gender=gender,birthday=birthday,idCardNumber=idCardNumber,phoneNumber=phoneNumber
        )
        obj = models.Patient.objects.get(userName=userName)
        # obj.collectList.remove('-1')
        obj.save()
        res['retCode'] = 1
        res['message'] = '注册成功'

    else:
        res['retCode'] = 0
        res['message'] = '用户名已注册'

    return JsonResponse({'register': res})

@csrf_exempt
def docter_register(request):
    userName = request.POST.get('userName', 'username')
    password = request.POST.get('password', 'xxx')
    email = request.POST.get('email', '未注册')

    realName = request.POST.get('realName','xxx')
    phoneNumber = request.POST.get('phoneNumber','xxx')
    idCardNumber = request.POST.get('idCardNumber','xxx')
    gender = request.POST.get('gender','x')
    birthday = dateutil.parser.parse(request.POST.get('birthday','2000-01-01'))

    college = request.POST.get('college','Peking')
    degree = request.POST.get('degree','Peking')


    res = {'retCode': 0, 'message': ''}

    obj = models.Doctor.objects.filter(userName=userName)
    if obj.count() == 0:

        models.Doctor.objects.create(
            userName=userName, password=password,email=email,realName=realName,
            gender=gender,birthday=birthday,idCardNumber=idCardNumber,phoneNumber=phoneNumber
        )
        obj = models.Doctor.objects.get(userName=userName)
        # obj.collectList.remove('-1')
        obj.save()
        res['retCode'] = 1
        res['message'] = '注册成功'

    else:
        res['retCode'] = 0
        res['message'] = '用户名已注册'

    return JsonResponse({'register': res})

@csrf_exempt
def login(request):
    userName = request.POST.get('userName', 'username')
    password = request.POST.get('password', 'xxx')
    type = request.POST.get('type')
    res = {'retCode': -1, 'message': ''}
    print("userName = {}, password = {}".format(userName,password))

    if type == 'patient':
        obj = models.Patient.objects.filter(userName=userName)
        if obj.count() == 0:
            res['retCode'] = 0
            res['message'] = '用户不存在'
            print('用户不存在')
        else:
            obj = models.Patient.objects.get(userName=userName)
            if obj.password == password:
                res['retCode'] = 1
                res['message'] = '成功登录'
                print("登陆成功")
            else:
                res['retCode'] = 2
                res['message'] = '用户名或密码错误'
                print("密码错误")
    elif type == 'doctor':
        obj = models.Doctor.objects.filter(userName=userName)
        if obj.count() == 0:
            res['retCode'] = 0
            res['message'] = '用户不存在'
            print('用户不存在')
        else:
            obj = models.Doctor.objects.get(userName=userName)
            if obj.password == password:
                res['retCode'] = 1
                res['message'] = '成功登录'
                print("登陆成功")
            else:
                res['retCode'] = 2
                res['message'] = '用户名或密码错误'
                print("密码错误")


    return JsonResponse({'login': res})


@csrf_exempt
def patient_info(request):
    pass



