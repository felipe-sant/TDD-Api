import pandas as pd

def getGoldData():
    df = pd.read_parquet(f'data/gold/dados_de_acoes.parquet')
    return df