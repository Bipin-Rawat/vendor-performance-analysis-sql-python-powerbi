import pandas as pd
import os
import time  
from sqlalchemy import create_engine
import logging

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",  
    filemode="a"
)
engine=create_engine("sqlite:///inventory.db")

def load_raw_data():
    '''this function will load CSVs as dataFrame and ingest into db'''   
    start=time.time()   
    for file in os.listdir("data"):
        if '.csv' in file:
            df=pd.read_csv('data/'+file)
            logging.info(f"ingesting {file} in db")
            ingest_db(df,file[:-4],engine)
    end=time.time()
    total_time=(end-start)/60     
    logging.info('------------ingestion complete------------') 
    logging.info(f'\ntotal time taken:{total_time} minutes')   

def ingest_db(df,table_name,engine):
    '''this function will ingest the dataFrame into dataBase table'''
    df.to_sql(table_name,con=engine,if_exists='replace',index=False)

if __name__=='__main__':
    load_raw_data()