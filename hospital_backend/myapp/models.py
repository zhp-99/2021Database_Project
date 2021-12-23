from django.db import models

# Create your models here.

#患者类
class Patient(models.Model):
    #默认生成一个名为id的自增列，该id为主键
    #userName不可变
    userName = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=50,default='x')
    email = models.CharField(max_length=32,default="未注册")

    realName = models.CharField(max_length=32,default='x')
    gender = models.CharField(max_length=2,default='x')
    birthday = models.DateField(null=True)
    idCardNumber = models.CharField(max_length=18,unique=True,default='x')
    phoneNumber = models.CharField(max_length=11,unique=True,default='x')


#医生类
class Doctor(models.Model):
    #默认生成一个名为id的自增列，该id为主键
    #userName不可变
    userName = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=50,default='x')
    email = models.CharField(max_length=32,default="未注册")

    realName = models.CharField(max_length=32,default='x')
    gender = models.CharField(max_length=2,default='x')
    birthday = models.DateField(null=True)
    idCardNumber = models.CharField(max_length=18,unique=True,default='x')
    phoneNumber = models.CharField(max_length=11,unique=True,default='x')
    college = models.CharField(max_length=32, default='Peking')
    degree = models.CharField(max_length=32, default='Peking')

    office = models.ForeignKey('Office',on_delete=models.CASCADE,null=True)
    is_leader = models.BooleanField()

#预约表
class Appointment(models.Model):
    pName = models.CharField(max_length=32)
    dName = models.CharField(max_length=32)
    date = models.DateField()

#处方表
class Prescription(models.Model):
    pName = models.CharField(max_length=32)
    dName = models.CharField(max_length=32)
    date = models.DateField()
    medical = models.CharField(max_length=32)

#病历表，一个病历代表一次治疗，一次治疗会有一个处方,查询能通过病历的外码找到相应处方
class MedicalRecord(models.Model):
    pName = models.CharField(max_length=32)
    dName = models.CharField(max_length=32)
    date = models.DateField()
    prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE)

#科室表
class Office(models.Model):
    #科室以名称区分
    name = models.CharField(max_length=32,primary_key=True)
    leader_username = models.CharField(max_length=32,null=True)
    description = models.CharField(max_length=100,null=True)


