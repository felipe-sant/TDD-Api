import json
import pandas as pd

def getBronzeData(symbol):
    with open('data/bronze/' + symbol + '.json') as f:
        data = json.load(f)

    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, dict):
        df = pd.DataFrame([data])
    else:
        raise ValueError("Estrutura JSON não suportada")
    
    return df