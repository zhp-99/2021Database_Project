from django.forms import model_to_dict
from django.shortcuts import render
from . import models
from . import function
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

# Create your views here.

@csrf_exempt
def patient_register(request):
    userName = request.POST.get('userName', 'username')
    realName = request.POST.get('realName', 'xxx')
    password = request.POST.get('password', 'xxx')
    email = request.POST.get('email', '未注册')
    phoneNumber = request.POST.get('phoneNumber','xxx')
    idCardNumber = request.POST.get('idCardNumber','xxx')
    gender = request.POST.get('gender','x')
    birthday = dateutil.parser.parse(request.POST.get('birthday','2000-01-01'))

    res = {'retCode': 0, 'message': ''}

    obj = models.Patient.objects.filter(userName=userName)
    if obj.count() == 0:

        models.Patient.objects.create(
            userName=userName, password=password, email=email, realName=realName,
            gender=gender, birthday=birthday, idCardNumber=idCardNumber, phoneNumber=phoneNumber
        )
        obj = models.Patient.objects.get(userName=userName)
        # obj.collectList.remove('-1')
        obj.save()
        res['retCode'] = 1
        res['message'] = '注册成功'

    else:
        res['retCode'] = 0
        res['message'] = '用户名已注册'

    return JsonResponse(res)

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
    office_name = request.POST.get('office','x')
    is_leader = int(request.POST.get('leader',0))

    res = {'retCode': 0, 'message': ''}

    obj = models.Doctor.objects.filter(userName=userName)
    if obj.count() == 0:
        office = models.Office.objects.filter(name=office_name)
        if office.count() == 0:
            office = None
        else:
            office = office[0]
            if is_leader == True:
                office.leader_username = userName
                office.save()

        models.Doctor.objects.create(
            userName=userName, password=password,email=email,realName=realName,
            gender=gender,birthday=birthday,idCardNumber=idCardNumber,phoneNumber=phoneNumber,
            college=college,degree=degree,office=office,is_leader=is_leader

        )
        obj = models.Doctor.objects.get(userName=userName)
        # obj.collectList.remove('-1')
        obj.save()
        res['retCode'] = 1
        res['message'] = '注册成功'

    else:
        res['retCode'] = 0
        res['message'] = '用户名已注册'

    return JsonResponse(res)


# 注册（使用了Django内助的邮箱验证功能）
@csrf_exempt
def register(request):
    userName = request.POST.get('userName', 'username')
    password = request.POST.get('password', 'xxx')
    email = request.POST.get('email', 'undefined')
    userType = request.POST.get('userType', 'patient')
    res = {'retCode': 0, 'message': ''}

    obj = models.UserModel.objects.filter(userName=userName)
    objmail = models.UserModel.objects.filter(email=email)

    if obj.count() == 0 and objmail.count() == 0:
        mailret = send_mail('PkuHospital注册', '您正在进行PkuHospital注册，如果不是您亲自操作，请及时联系本邮箱',
                            'se_5group@163.com', [email], fail_silently=False)

        if mailret == 1:
            if userType == 'patient':
                models.PatientModel.objects.create(userName=userName, password=password,email=email)
                obj = models.PatientModel.objects.get(userName=userName)
            elif userType == 'doctor':
                models.DoctorModel.objects.create(userName=userName, password=password,email=email)
                obj = models.DoctorModel.objects.get(userName=userName)
            obj.save()
            res['retCode'] = 1
            res['message'] = '注册成功'

        else:
            res['retCode'] = 2
            res['message'] = '请输入正确的邮箱地址'

    else:
        res['retCode'] = 0
        res['message'] = '用户名或邮箱已注册'

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
def patient_homepage_info(request):
    userName = request.POST.get('userName', 'username')
    patientCondition = request.POST.get('patientCondition', 'usual')
    res = function.patient_info(userName)
    res.update(function.patient_appointment_count(userName))
    res.update(function.patient_appointments(userName))
    res.update(function.patient_medical_records(userName))
    if patientCondition == 'usual':
        res.update(function.get_office_index())
    if patientCondition == 'fever':
        res.update(function.get_office_fever())
    print(res)
    return JsonResponse(res)

@csrf_exempt
def doctor_homepage_info(request):
    userName = request.POST.get('userName', 'username')
    res = function.doctor_info(userName)
    res.update(function.today_appointment_list(userName))
    res.update(function.history_patient_list(userName))
    print(res)
    return JsonResponse(res)


@csrf_exempt
def medical_record_detail_info(request):
    pid = request.POST.get('id', 'id')
    res = {'retCode': -1, 'message': ''}
    res.update(function.prescription_info(pid))
    print('response is', res)
    return JsonResponse(res)


@csrf_exempt
def office_info(request):
    res = {'retCode': -1, 'message': ''}
    officeName = request.POST.get('officeName', 'officename')
    res.update(function.get_doctor_index(officeName))
    return JsonResponse(res)


@csrf_exempt
def reservation_calendar_info(request):
    userName = request.POST.get('userName', 'username')
    res = {'retCode': -1, 'message': ''}
    dateAndReservation = list()
    today = date.today()
    for i in range(31):
        dic = {'date': str(today), 'reserve': 30-len(function.appointments_by_doctor_date(userName, today))}
        dateAndReservation.append(dic)
        today += timedelta(days=1)
    res['CalendarList'] = dateAndReservation
    return JsonResponse(res)


@csrf_exempt
def patient_info(request):
    userName = request.POST.get('userName', 'username')
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
        res['realName'] = obj.realName
        res['gender'] = obj.gender
        res['birthday'] = obj.birthday
        res['phoneNumber'] = obj.phoneNumber
        print('查询成功')

    return JsonResponse(res)

@csrf_exempt
def doctor_info(request):
    userName = request.POST.get('userName', 'username')
    doctor = models.Doctor.objects.filter(userName=userName)
    res = {'retCode': -1, 'message': ''}
    if doctor.count() == 0:
        res['retCode'] = 0
        res['message'] = '用户不存在'
        print('用户不存在')
    else:
        doctor = doctor[0]

        res['retCode'] = 1
        res['message'] = '查询成功'
        res['userName'] = doctor.userName
        res['realName'] = doctor.realName
        res['gender'] = doctor.gender
        res['birthday'] = doctor.birthday
        res['phoneNumber'] = doctor.phoneNumber
        res['college'] = doctor.college
        res['degree'] = doctor.degree
        res['is_leader'] = doctor.is_leader
        res['office'] = doctor.office.name
        print('查询成功')

    return JsonResponse(res)


@csrf_exempt
def modify_patient(request):
    userName = request.POST.get('userName')
    password = request.POST.get('password')
    email = request.POST.get('email')
    phoneNumber = request.POST.get('phoneNumber')

    obj = models.Patient.objects.get(userName=userName)
    if password is not None:
        obj.password = password
    if email is not None:
        obj.email = email
    if phoneNumber is not None:
        obj.phoneNumber = phoneNumber

    obj.save()

    res = {'retCode': 1, 'message': '修改成功'}
    return JsonResponse(res)

@csrf_exempt
def modify_doctor(request):
    userName = request.POST.get('userName')
    password = request.POST.get('password')
    email = request.POST.get('email')
    phoneNumber = request.POST.get('phoneNumber')

    obj = models.Doctor.objects.get(userName=userName)
    if password is not None:
        obj.password = password
    if email is not None:
        obj.email = email
    if phoneNumber is not None:
        obj.phoneNumber = phoneNumber

    obj.save()

    res = {'retCode': 1, 'message': '修改成功'}
    return JsonResponse(res)


@csrf_exempt
def make_appointment(request):
    pName = request.POST.get('pName')
    dName = request.POST.get('dName')
    date = dateutil.parser.parse(request.POST.get('date'))
    print('有挂号需求', pName, dName, date)
    res = {'retCode': -1, 'message': ''}

    patient_doc_date = models.Appointment.objects.filter(pName=pName, dName=dName, date=date)
    if patient_doc_date.count()>0:
        res = {'retCode': 2, 'message': '您已经挂过此号'}
        return JsonResponse(res)
    else:
        doc_today_apps = models.Appointment.objects.filter(dName=dName, date=date)

    if doc_today_apps.count()>=30:
        res = {'retCode': 3, 'message': '该日无号'}
        return JsonResponse(res)
    else:
        obj = models.Appointment.objects.create(pName=pName, dName=dName, date=date)
        obj.save()
        res = {'retCode': 1, 'message': '预约成功'}
        return JsonResponse(res)


@csrf_exempt
def doctor_appointments(request):
    userName = request.POST.get('userName')
    app_list = models.Appointment.objects.filter(dName=userName)
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

@csrf_exempt
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

@csrf_exempt
def patient_appointments(request):
    userName = request.POST.get('userName')
    app_list = models.Appointment.objects.filter(pName=userName)
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

@csrf_exempt
def patient_appointments_by_date(request):
    userName = request.POST.get('userName')
    date = request.POST.get('date')
    app_list = models.Appointment.objects.filter(pName=userName,date=date)
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


@csrf_exempt
def make_mr(request):
    pName = request.POST.get('pName')
    dName = request.POST.get('dName')
    date = dateutil.parser.parse(request.POST.get('date'))
    medical = request.POST.get('medical')

    prescription = models.Prescription.objects.create(pName=pName,dName=dName,date=date,medical=medical)
    prescription.save()
    mr = models.MedicalRecord.objects.create(pName=pName,dName=dName,date=date,prescription=prescription)
    mr.save()
    res = {'retCode': 1, 'message': '预约成功'}
    return JsonResponse(res)

@csrf_exempt
def patient_mrs(request):
    userName = request.POST.get('userName')
    mr_list = models.MedicalRecord.objects.filter(pName=userName)
    res_list = []
    for mr in mr_list:
        mr_dict = model_to_dict(mr)
        dName = mr.dName
        pName = mr.pName
        mr_dict['dRealName'] = models.Doctor.objects.get(userName=dName).realName
        mr_dict['pRealName'] = models.Patient.objects.get(userName=pName).realName
        res_list.append(mr_dict)
    res = {'retCode': 1}
    res['mrList'] = res_list
    return JsonResponse(res)

@csrf_exempt
def patient_mrs_by_date(request):
    userName = request.POST.get('userName')
    date = request.POST.get('date')
    mr_list = models.MedicalRecord.objects.filter(pName=userName,date=date)
    res_list = []
    for mr in mr_list:
        mr_dict = model_to_dict(mr)
        dName = mr.dName
        pName = mr.pName
        mr_dict['dRealName'] = models.Doctor.objects.get(userName=dName).realName
        mr_dict['pRealName'] = models.Patient.objects.get(userName=pName).realName
        res_list.append(mr_dict)
    res = {'retCode': 1}
    res['mrList'] = res_list
    return JsonResponse(res)

@csrf_exempt
def office_register(request):
    name = request.POST.get('name')
    leader_username = request.POST.get('leader_username')
    description = request.POST.get('description')
    res = {'retCode': -1}
    office = models.Office.objects.create(name=name,leader_username=leader_username,description=description)
    office.save()
    if leader_username is not None:
        doctor = models.Doctor.objects.filter(userName=leader_username)
        if doctor.count() == 0:
            res['retCode'] = 2
        else:
            #把科长信息修改了
            doctor = doctor[0]
            doctor.is_leader = True
            doctor.office = office
            doctor.save()
            res['retCode'] = 1

    return JsonResponse(res)


@csrf_exempt
def getOfficeIndex(request):
    userName = request.POST.get('userName')
    retdata = {}
    offices = models.Office.objects.values()
    office_list = list(offices)
    res_list = list()
    for office in office_list:
        doctor_num = len(models.Office.objects.raw('SELECT * FROM myapp_work WHERE office_name = %s', [office['name']]))
        res_list.append({'office_name': office['name'], 'doctor_num': doctor_num})
    retdata['userName'] = userName
    retdata['Officelist'] = res_list
    return JsonResponse(retdata)

@csrf_exempt
def getCourseIndex(request):
    SchoolName = request.POST.get('schoolname')
    print(SchoolName)
    which_school = models.School.objects.get(school_name = SchoolName)
    courses = models.Course.objects.filter(sid = which_school.id).values()
    retdata = {}
    retdata['courselist'] = list(courses)
    return JsonResponse(retdata)

@csrf_exempt
def getQuestionIndex(request):
    CourseName = request.POST.get('coursename')
    print(CourseName)
    which_course = models.Course.objects.get(course_name = CourseName)
    questions = models.Question.objects.filter(cid = which_course.id).values()
    retdata = {}
    retdata['questionlist'] = list(questions)
    return JsonResponse(retdata)

@csrf_exempt
def addQuestion(request):
    CourseName = request.POST.get('coursename')
    which_course = models.Course.objects.get(course_name = CourseName)
    q_publisher = request.POST.get('publisher')
    q_title = request.POST.get('title')
    q_content = request.POST.get('content')
    q1 = models.Question(cid = which_course.id, publisher = q_publisher, title = q_title, content = q_content)
    q1.save()
    res = {'retCode': 0, 'message': ''}
    if(q1.id > 0 ):
        res['retCode'] = 0
        res['message'] = '成功添加问题'
    else:
        res['retCode'] = 1
        res['message'] = '添加问题失败'
    return JsonResponse({'addQuestion':res})

@csrf_exempt
def addReply(request):
    rep = request.POST.get('replyer')
    ct = request.POST.get('reply_content')
    Qid = request.POST.get('qid')
    p1 = models.Reply(proNum = 0, conNum = 0, replyer = rep, qid = Qid, content = ct)
    p1.save()

    res = {'retCode': 0, 'message': ''}
    if(p1.id > 0 ):
        res['retCode'] = 0
        res['message'] = '成功添加回复'
    else:
        res['retCode'] = 1
        res['message'] = '添加回复失败'
    return JsonResponse(res)

@csrf_exempt
def getAnswerList(request):#返回answerList和当前问题的内容
    Qid = request.POST.get('question_id')
    ques =  models.Question.objects.get(id = Qid)
    replys = models.Reply.objects.filter(qid = Qid).values()
    retdata = {}
    retdata['answerlist'] = list(replys)
    retdata['question'] = {'title':ques.title, 'content':ques.content}

    return JsonResponse(retdata)

@csrf_exempt
def likeAnswer(request):
    rid = request.POST.get('answer_id')
    rep = models.Reply.objects.get(id = rid)
    rep.proNum = rep.proNum +1
    rep.save()
    res = {'retCode': 0, 'message': 'OK'}
    return JsonResponse(res)

@csrf_exempt
def dislikeAnswer(request):
    CourseName = request.POST.get('coursename')
    which_course = models.Course.objects.get(course_name = CourseName)
    q_publisher = request.POST.get('publisher')
    q_title = request.POST.get('title')
    q_content = request.POST.get('content')
    q1 = models.Question(cid = which_course.id, publisher = q_publisher, title = q_title, content = q_content)
    q1.save()
    res = {'retCode': 0, 'message': ''}
    if(q1.id > 0 ):
        res['retCode'] = 0
        res['message'] = '成功添加问题'
    else:
        res['retCode'] = 1
        res['message'] = '添加问题失败'
    return JsonResponse({'addQuestion':res})

@csrf_exempt
def openSchool(request):
    schoolName = request.POST.get('school', '信息科学技术学院')
    courses = [ {'date': '更新于 2021-06-03 15:56:00', 'title': 'course1 from backend openSchool'}, {'date': '更新于 2021-06-03 15:56:00', 'title': 'course2 from backend openSchool'} ]
    courses = json.JSONEncoder(ensure_ascii=False).encode(courses)
    print("将courses发回前端")
    return JsonResponse({'retCode': 1, 'courses': courses})


@csrf_exempt
def openCourse(request):
    courseName = request.POST.get('course', '软件工程')
    questions = [
        {'date': '更新于 2021-06-03 15:56:00', 'title': 'Question1 from backend', 'content': 'c1', 'stars': 58, 'link': 'l1'},
        {'date': '更新于 2021-06-03 15:56:00', 'title': 'Question2 from backend', 'content': 'c2', 'stars': 66, 'link': 'l2'},
        ]
    questions = json.JSONEncoder(ensure_ascii=False).encode(questions)
    return JsonResponse({'retCode': 1, 'questions': questions})


@csrf_exempt
def openQuestion(request):
    courseName = request.POST.get('question', '默认问题')

    curQuestion = { 'publisher': 'alice', 'title': 'ahhhhhhh', 'detail': '咆哮啊啊啊', 'proNum': 2, 'conNum': 1, 'subscribeNum': 3,}
    curQuestion = json.JSONEncoder(ensure_ascii=False).encode(curQuestion)
    curAnswer = { 'publisher': 'bob', 'title': 'hahahahahaha', 'detail': '哈哈哈哈哈', 'proNum': 6, 'conNum': 6, 'subscribeNum': 12,}
    # 现在只显示一个问题和一个答案, 如果我们想要看一个问题的所有答案, 只需要搞成list of dict 就可以了 暂时不实现
    curAnswer = json.JSONEncoder(ensure_ascii=False).encode(curAnswer)

    return JsonResponse({'retCode': 1, 'curQuestion': curQuestion, 'curAnswer': curAnswer})


@csrf_exempt
def submitQuestion(request):
    questionTitle = request.POST.get('title', '缺少标题')
    questionDate1 = request.POST.get('date1', '0000-00-00')
    questionDate2 = request.POST.get('date2', '00:00:00')
    questionDetail = request.POST.get('detail', '缺少问题描述')
    # 此处应该把问题存到数据库里
    return JsonResponse({'retCode': 1, 'title': questionTitle, 'detail': questionDetail})

'''
这个关注课程功能不仅不重要而且很麻烦我先不写了。
@csrf_exempt
def AddFollowCourse(request):
    course_name = request.POST.get('course_name')
    user_name = request.POST.get('userName')
    user_obj = models.UserModel.objects.get(userName = user_name)
    user_obj.
'''
