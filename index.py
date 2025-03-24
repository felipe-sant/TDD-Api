from dotenv import load_dotenv
import os
from functions.loadBronzeData import loadBronzeData
from functions.loadSilverData import loadSilverData
from functions.loadGoldData import loadGoldData
from functions.getGoldData import getGoldData

load_dotenv()

token = os.getenv('API_TOKEN')

token = token,
symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA", "PYPL", "SPOT", "SHOP"]

loadBronzeData(token, symbols)
loadSilverData(symbols)
loadGoldData()

for symbol in symbols:
    df = getGoldData()
    print()
    df_filtrada = df[df['empresa'] == symbol]
    print(df_filtrada)