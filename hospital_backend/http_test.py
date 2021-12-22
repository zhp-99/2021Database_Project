import requests

url = 'http://localhost:8000/myapp/doctor/info'
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
r = requests.post(url,data=login_data)
print(r.text)