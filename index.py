from dotenv import load_dotenv
import os
from functions.loadBronzeData import loadBronzeData
from functions.loadSilverData import loadSilverData
from functions.loadGoldData import loadGoldData
from functions.getGoldData import getGoldData

load_dotenv()

token = os.getenv('API_TOKEN')

data = {
    "token": token,
    "url": "https://api.stockdata.org/v1/data/eod",
    "symbols": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA", "PYPL", "SPOT", "SHOP"],
}

# loadBronzeData(data)
# loadSilverData(data)
# loadGoldData()

for symbol in data["symbols"]:
    df = getGoldData()
    print()
    df_filtrada = df[df['empresa'] == symbol]
    print(df_filtrada)