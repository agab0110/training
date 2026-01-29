import requests

url = "http://web-08.challs.olicyber.it/login"

data = {
    "username": "admin",
    "password": "admin"
}

headers = {"Accept": "application/x-www-form-urlencoded"}

response = requests.post(url, data=data, headers=headers)

print(response.text)