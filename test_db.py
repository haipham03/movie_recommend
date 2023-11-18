import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv
import turicreate as tc

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT)

cursor = conn.cursor()

df = pd.read_sql('SELECT * FROM movies', conn)

model = tc.load_model("models/recommendations.model")

items = tc.SFrame(data=df)