from functions.getBronzeData import getBronzeData
import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def loadSilverData(data):
    bruteData = {}
    
    for symbol in data["symbols"]:
        bronzeData = getBronzeData(symbol)
        bruteData[symbol] = bronzeData["data"]
    
    formatedData = []
    
    for symbol in bruteData:
        for data in bruteData[symbol]:
            json = {
                "Empresa": symbol,
                "Data": data['date'],
                "Alta": data['high'],
                "Baixa": data['low'],
                "Fechamento": data['close'],
            }
            formatedData.append(json)
    
    df = pd.DataFrame(formatedData)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f'data/silver/dados_de_acoes.parquet')