from services.apiConnection import apiConnection
from datetime import datetime, timedelta
import json

def loadBronzeData(token, symbols):
    for symbol in symbols:
        params = {
            "api_token": token,
            "symbols": symbol,
            "date_from": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
            "date_to": datetime.now().strftime("%Y-%m-%d"),
            "format": "json"
        }
        response = apiConnection(params)
        if response:
            with open(f"data/bronze/{symbol}.json", "w") as file:
                json.dump(response, file, indent=3)
        else:
            print("Error loading data")
            return
        
    print("Bronze data loaded successfully")