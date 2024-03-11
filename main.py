"""Module for looking up Epic Games Accounts"""
import re  # For regex
import requests

from account import ExternalAuth

URL = "https://api.proswapper.xyz"

id_or_name = input("Enter Epic Account ID or Display Name: ")

url = f"{URL}/external/name/{id_or_name}"  # URL for searching by Display Name
if re.search(r'^[0-9a-f]{32}$', id_or_name):  # Checks if the input is an ID
    url = f"{URL}/external/id/{id_or_name}"

response = requests.request("GET", url, timeout=10)
result = response.json()
if len(result) == 0:
    print("No account found")
else:
    if len(result[0]["externalAuths"].items()) == 0:
        print("No external auths found")
    else:
        for key, value in result[0]["externalAuths"].items():
            print(ExternalAuth(key, value).to_string())
