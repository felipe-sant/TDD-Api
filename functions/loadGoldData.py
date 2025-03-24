from functions.getSilverData import getSilverData
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def loadGoldData():
    df_silver = getSilverData()
    
    formatedData = []
    
    for index in df_silver.index:
        json = {
            "empresa": df_silver['enterprise'][index],
            "dia": df_silver['date'][index],
            "preco": round(float((df_silver['low'][index] + df_silver['high'][index]) / 2), 2)
        }
        formatedData.append(json)
        
    df = pd.DataFrame(formatedData)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f'data/gold/dados_de_acoes.parquet')
    