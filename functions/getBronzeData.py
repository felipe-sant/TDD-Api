import json
import pandas as pd

def getBronzeData(symbol):
    with open('data/bronze/' + symbol + '.json') as f:
        data = json.load(f)

    return data