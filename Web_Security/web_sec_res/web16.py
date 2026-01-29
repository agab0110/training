import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base = "http://web-16.challs.olicyber.it/"
visited = set()
to_visit = [base]

while to_visit:
    url = to_visit.pop()

    if url in visited:
        continue
    visited.add(url)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    h1 = soup.find("h1")
    if h1 and "flag{" in h1.text:
        print("FLAG:", h1.text)
        break

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and href.startswith("/page?p="):
            full = urljoin(base, href)
            if full not in visited:
                to_visit.append(full)
