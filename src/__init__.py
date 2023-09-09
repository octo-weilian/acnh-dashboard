import streamlit as st
from sqlalchemy import create_engine 
from pathlib import Path
import pandas as pd
import requests
from datetime import datetime

from src.db import load_tables

sqlite_db = "sqlite:///acnh.db"
alchemy_engine = create_engine(sqlite_db)
db_connection = alchemy_engine.connect()

if not db_connection.closed:
    load_tables(path="./src/data",engine=alchemy_engine)
    
@st.cache_data(ttl=600)
def get_data(query):
    df =  pd.read_sql(sql=query,con=db_connection)
    return df

def get_ts():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")
