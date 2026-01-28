import requests
from bs4 import BeautifulSoup, Comment

url = "http://web-14.challs.olicyber.it"

html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

comment = soup.find_all(string=lambda text: isinstance(text, Comment))

for c in comment:
    print(c)