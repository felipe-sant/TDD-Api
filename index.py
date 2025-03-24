from dotenv import load_dotenv
import os
from services.apiConnection import apiConnection
import json

load_dotenv()

token = os.getenv('API_TOKEN')

url = "https://api.stockdata.org/v1/data/eod"

params = {
    "api_token": token,
    "symbols": "AAPL",
}

response = json.dumps(apiConnection(url, params))

print(response)