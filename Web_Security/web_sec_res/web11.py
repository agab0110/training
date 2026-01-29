import requests
import json

base_url = "http://web-11.challs.olicyber.it"

session = requests.Session()

login_data = {
    "username": "admin",
    "password": "admin"
}

headers = {"Content-Type": "application/json"}

login_response = session.post(base_url + "/login", data = json.dumps(login_data), headers = headers)

print("Risposta login: " + login_response.text)

csrf = login_response.json()["csrf"]
print("Token CSRF:", csrf)

flag = ""

for i in range(4):
    flag_response = session.get(
        base_url + f"/flag_piece?index={i}&csrf={csrf}",
        #json={"csrf": csrf}
    )

    print(f"Risposta alla {i} iterazione:", flag_response.text)

    data = flag_response.json()

    csrf = data["csrf"]

    flag += data["flag_piece"]

print("Flag: " + flag)