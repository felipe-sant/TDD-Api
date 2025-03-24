import requests

def apiConnection(url, params):
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        return e