import requests

SERVER = 'http://127.0.0.1:5000/'
data = [{"first_name": "caleb", "last_name": "eghan", "password": "123"},
        {"first_name": "ben", "last_name": "hendeerson", "password": "321"},
        {"first_name": "frank", "last_name": "benkam", "password": "231"}]

for i in range(len(data)):
    response = requests.post(SERVER + "customer/" + str(i), data[i])
    print(response.json())

    response = requests.delete(SERVER + "customer/1")
    print(response)

    response = requests.get(SERVER + "customer/2")
    print(response.json())
