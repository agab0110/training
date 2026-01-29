import requests

url = "http://web-10.challs.olicyber.it"

response = requests.options(url)
print("Allow: " + response.headers.get("Allow"))

response = requests.get(url)
print("Get: " + str(response.status_code) + " " + response.text + " " + str(response.headers))

response = requests.post(url)
print("Post: " + str(response.status_code) + " " + response.text + " " + str(response.headers))

response = requests.put(url)
print("Put: " + str(response.status_code) + " " + response.text + " " + str(response.headers))

response = requests.patch(url)
print("Patch: " + str(response.status_code) + " " + response.text + " " + str(response.headers))

response = requests.delete(url)
print("Delete: " + str(response.status_code) + " " + response.text + " " + str(response.headers))