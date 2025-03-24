import requests

def apiConnection(params):
    try:
        response = requests.get("https://api.stockdata.org/v1/data/eod", params=params)
        return response.json()
    except Exception as e:
        return e