import requests

SERVER = 'http://127.0.0.1:5000/'
connect = requests.post(SERVER + '/customer/caleb',
                        {"first_name": "caleb", "last_name": "eghan", "set_password": "1234"})
print(connect.json())

input()
connect2 = requests.get(SERVER + '/customer/caleb')
print(connect2.json())

# connect2 = requests.get(SERVER + '/customer/ben')
# print(connect2.json())
# , {"first_name": "caleb", "last_name": "eghan", "set_password": "123"}
