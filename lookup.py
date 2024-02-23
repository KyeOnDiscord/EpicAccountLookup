"""Module for looking up Epic Games Accounts"""

import requests
from account import Account, ExternalAuth

URL = "https://account-public-service-prod.ol.epicgames.com"


def lookup_account_by_id(bearer, account_id):
    """Lookup an Epic Games Account by its 32 character long account ID"""
    url = f"{URL}/account/api/public/account?accountId={account_id}"

    headers = {
        'Authorization': f'Bearer {bearer}'
    }

    response = requests.request("GET", url, headers=headers, timeout=10)
    result = response.json()[0]
    external_auths = []
    for key, value in result["externalAuths"].items():
        e_auth = ExternalAuth(key, value)
        external_auths.append(e_auth)
        print(e_auth.ToString())
    if len(external_auths) == 0:
        print("No external auths found")
    return Account(result["displayName"], result["id"], external_auths)


def lookup_account_by_display_name(bearer, display_name):
    """Lookup an Epic Games Account by its display name"""
    url = f"{URL}/account/api/public/account/displayName/{display_name}"
    headers = {
        'Authorization': f'Bearer {bearer}'
    }
    response = requests.get(url, headers=headers, timeout=10)
    print(response.text)
