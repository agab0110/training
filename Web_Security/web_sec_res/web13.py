import requests
from bs4 import BeautifulSoup
url = "http://web-13.challs.olicyber.it"

html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

letters = [span.text for span in soup.find_all("span", class_="red")]

flag = "flag{" + "".join(letters) + "}"

print(flag)