import pandas as pd
from sqlalchemy import create_engine
from time import time

conn_str='postgresql://aalonso:aalonso@localhost:5432/nyc_taxi'
engine=create_engine(conn_str)
df_iter=pd.read_csv("data_download/yellow_tripdata_2021-01.csv",iterator=True,chunksize=100000)

while True:
    t_start_time=time()
    df=next(df_iter)
    df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(name='nyc_table', con=engine, if_exists='append', index=False)
    t_end_time=time()
    print("Inserting df it took %.3f second" %(t_end_time-t_start_time))