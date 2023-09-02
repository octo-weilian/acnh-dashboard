import streamlit as st
from sqlalchemy import create_engine 
from pathlib import Path
import pandas as pd
import requests
from src.db import load_tables

postgres_uri = "postgresql+psycopg2://postgres:postgres@localhost:5432/acnh"
alchemy_engine = create_engine(postgres_uri)
db_connection = alchemy_engine.connect()

if not db_connection.closed:
    load_tables(path="./data",engine=alchemy_engine)

@st.cache_data(ttl=600)
def get_data(query):
    df =  pd.read_sql(sql=query,con=db_connection)
    return df


