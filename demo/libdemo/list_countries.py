import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details! Error -->", resp.reason)
    exit()

countries = resp.json()  # Convert JSON response to dict

for c in countries:
    name = c['name']['common']
    capital = c['capital'][0] if 'capital' in c else 'None'
    population = c['population']
    area = c['area']
    print(f"{name:50} {capital:30}  {population:10} {area:10}")






