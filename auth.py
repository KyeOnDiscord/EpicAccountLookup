"""Epic Games Authentication Module"""
import requests


def get_bearer_token():
    """Gets the client_credentials for fortnitePCGameClient from Epic Games' OAuth API."""
    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

    payload = 'grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # fortnitePCGameClient, base64 encoded of 'ec684b8c687f479fadea3cb2ad83f5c6:e1f31c211f28413186262d37a13fc84d'
        "Authorization": "Basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Error getting bearer token, status:", response.status_code)
