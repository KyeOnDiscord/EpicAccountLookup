import requests
from account import Account, ExternalAuth

def LookupAccountByID(bearer, accountID):
    url = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account?accountId={accountID}"

    payload = {}
    headers = {
    'Authorization': f'Bearer {bearer}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()[0]
    externalAuths = []
    for key,value in result["externalAuths"].items():
        eAuth = ExternalAuth(key, value)
        externalAuths.append(eAuth)
        print(eAuth.ToString())
    if len(externalAuths) == 0:
        print("No external auths found")
    return Account(result["displayName"], result["id"],externalAuths)

def LookupAccountByName(bearer, displayName):
    url = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/displayName/{displayName}"
    headers = {
    'Authorization': f'Bearer {bearer}'
    }
    response = requests.get(url, headers=headers)
    print(response.text)