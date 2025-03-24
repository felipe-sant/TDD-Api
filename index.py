from dotenv import load_dotenv
import os
from functions.loadBronzeData import loadBronzeData
import pandas as pd
from functions.loadSilverData import loadSilverData

load_dotenv()

token = os.getenv('API_TOKEN')

data = {
    "token": token,
    "url": "https://api.stockdata.org/v1/data/eod",
    "symbols": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA", "PYPL", "SPOT", "SHOP"],
}

# loadBronzeData(data)
loadSilverData(data)

for symbol in data["symbols"]:
    df = pd.read_parquet('data/silver/AAPL.parquet')
    print()
    print(symbol)
    print(df)