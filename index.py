from dotenv import load_dotenv
import os
from services.apiConnection import apiConnection
import json
from datetime import datetime, timedelta
from functions.loadBronzeData import loadBronzeData

load_dotenv()

token = os.getenv('API_TOKEN')

data = {
    "token": token,
    "url": "https://api.stockdata.org/v1/data/eod",
    "symbols": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA", "PYPL", "SPOT", "SHOP"],
}

loadBronzeData(data)
