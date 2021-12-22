import requests

regist_data = {
    'userName':'zhp',
    'password':'123',
    'realName':'zhang',
    'phoneNumber':'18811731213',
    'idCardNumber':'123456',
    'gender':'男',
    'birthday':'1999-11-12'
}
login_data = {
    'userName':'zhp',
    'password':'123',
    'type':'doctor'
}
info_data = {
    'userName':'zhp'
}
modify_data = {
    'userName':'zhp',
    'password':'125'
}
app_data = {
    'pName':'zhp',
    'dName':'zhp'
}
# url = 'http://localhost:8000/myapp/patient/register'
# for i in range(5):
#     regist_data = {
#         'userName': 'p'+str(i),
#         'password': '123',
#         'realName': 'pr'+str(i),
#         'phoneNumber': 'pp'+str(i),
#         'idCardNumber': 'pi'+str(i),
#         'gender': '男',
#         'birthday': '1999-11-12'
#     }
#     r = requests.post(url,data=regist_data)
#     print(r.text)
#
# url = 'http://localhost:8000/myapp/doctor/register'
# for i in range(5):
#     regist_data = {
#         'userName': 'd'+str(i),
#         'password': '123',
#         'realName': 'dr'+str(i),
#         'phoneNumber': 'dp'+str(i),
#         'idCardNumber': 'di'+str(i),
#         'gender': '男',
#         'birthday': '1999-11-12'
#     }
#     r = requests.post(url,data=regist_data)
#     print(r.text)

# url = 'http://localhost:8000/myapp/patient/makeAppointment'
# for i in range(3):
#     regist_data = {
#         'pName':'p'+str(i),
#         'dName':'d0',
#         'date':'2022-02-02'
#     }
#     r = requests.post(url,data=regist_data)
#     print(r.text)

url = 'http://localhost:8000/myapp/doctor/appointments'
doc_app_data = {
    'userName':'d0'
}
r = requests.post(url,data=doc_app_data)
print(r.text)

# url = 'http://localhost:8000/myapp/doctor/appointments/byDate'
# doc_app_data = {
#     'userName':'d0',
#     'date':'2022-02-02'
# }
# r = requests.post(url,data=doc_app_data)
# print(r.text)

# url = 'http://localhost:8000/myapp/doctor/makeMR'
# mr_data = {
#     'pName':'p0',
#     'dName':'d0',
#     'date':'2022-02-02',
#     'medical':'dead'
# }
# r = requests.post(url,data=mr_data)
# print(r.text)