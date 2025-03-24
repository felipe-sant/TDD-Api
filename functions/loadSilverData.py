from functions.getBronzeData import getBronzeData
import pyarrow as pa
import pyarrow.parquet as pq

def loadSilverData(data):
    for symbol in data["symbols"]:
        bronzeData = getBronzeData(symbol)
        table = pa.Table.from_pandas(bronzeData)
        pq.write_table(table, f'data/silver/{symbol}.parquet')