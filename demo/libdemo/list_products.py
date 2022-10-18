import requests
from bs4 import BeautifulSoup

with open("products.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")

for product in bs.find_all("product"):
    name = product.find("name").text
    price = product.find("price").text
    print(f"{name:30} {int(price):10}")
