from functions.getBronzeData import getBronzeData
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def loadSilverData(symbols):
    bruteData = {}
    
    for symbol in symbols:
        bronzeData = getBronzeData(symbol)
        bruteData[symbol] = bronzeData["data"]
    
    formatedData = []
    
    for symbol in bruteData:
        for data in bruteData[symbol]:
            json = {
                "enterprise": symbol,
                "open": data['open'],
                "date": data['date'],
                "high": data['high'],
                "low": data['low'],
                "close": data['close'],
                "volume": data['volume']
            }
            formatedData.append(json)
    
    df = pd.DataFrame(formatedData)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f'data/silver/dados_de_acoes.parquet')