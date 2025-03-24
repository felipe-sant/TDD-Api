import json
import pandas as pd

def getBronzeData(symbol):
    with open('data/bronze/' + symbol + '.json') as f:
        data = json.load(f)

    df = pd.DataFrame(data['data'])

    df['date'] = pd.to_datetime(df['date'])

    df_daily = df.resample('D', on='date').mean()[['low', 'high']]
    df_daily['low'] = df_daily['low'].fillna(0)
    df_daily['high'] = df_daily['high'].fillna(0)
    
    return df_daily