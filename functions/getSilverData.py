import pandas as pd

def getSilverData():
    df = pd.read_parquet(f'data/silver/dados_de_acoes.parquet')
    return df