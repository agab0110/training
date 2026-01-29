import requests
from bs4 import BeautifulSoup, Comment

base_url = "http://web-15.challs.olicyber.it"

html = requests.get(base_url)

soup = BeautifulSoup(html.text, 'html.parser')

urls = []

for script in soup.find_all("script"):
    src = script.get("src")
    if src:
        urls.append(src)

for link in soup.find_all("link"):
    href = link.get("href")
    if href:
        urls.append(href)

print("Risorse trovate: ", urls)

for u in urls:
    url = base_url + u
    response = requests.get(url)

    if "flag{" in response.text:
        print(response.text)