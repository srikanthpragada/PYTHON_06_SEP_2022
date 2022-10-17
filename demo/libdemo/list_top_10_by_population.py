import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details! Error -->", resp.reason)
    exit()

countries = resp.json()  # Convert JSON response to dict

for c in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    name = c['name']['common']
    population = c['population']
    print(f"{name:50}  {population:10}")
