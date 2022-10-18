import requests
from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

links = []
for a in bs.find_all("a"):
    if 'href' not in a.attrs:
        continue

    href = a['href']
    if 'javascript:void' in href or href == '#':
        continue

    if not href.startswith("http"):
        if href.startswith("/"):
            href = WEBSITE + href
        else:
            href = WEBSITE + '/' + href

    if not href in links:
        links.append(href)

for link in links:
    print(link)
