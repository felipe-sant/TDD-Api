from dotenv import load_dotenv
import os
from functions.loadBronzeData import loadBronzeData
from functions.loadSilverData import loadSilverData
from functions.loadGoldData import loadGoldData
from functions.getGoldData import getGoldData

load_dotenv()
token = os.getenv('API_TOKEN')
symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA", "PYPL", "SPOT", "SHOP"]

