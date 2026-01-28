import requests
from bs4 import BeautifulSoup
url = "http://web-12.challs.olicyber.it"

html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

print(soup.find_all('pre'))