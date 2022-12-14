import requests
from bs4 import BeautifulSoup
WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

links = []
for a in bs.find_all("a"):
    href = a['href']
    if 'javascript:void' in href:
        continue

    if not href.startswith("http"):
        href = WEBSITE + href

    if not href in links:
        links.append(href)

for link in links:
    print(link)

