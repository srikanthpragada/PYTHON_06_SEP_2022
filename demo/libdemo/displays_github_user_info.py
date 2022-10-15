import requests

resp = requests.get("https://api.github.com/users/gvanrossum")
if resp.status_code != 200:
    print("Sorry! Could not get details! Error -->", resp.reason)
    exit()

details = resp.json()  # Convert JSON response to dict
print(f"Name     = {details['name']}")
print(f"Company  = {details['company']}")
print(f"Location = {details['location']}")
print(f"Followers= {details['followers']}")





