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

#科室类
class Office(models.Model):
    description = models.CharField(max_length=100)

class Doc_Office(models.Model):
    doc_id = models.IntegerField()
    off_id = models.IntegerField()