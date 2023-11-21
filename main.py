import turicreate as tc
import os 
import schedule
import time

training = False  # Initialize the training flag

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


df = pd.read_sql_query("SELECT * FROM public.ratings", conn)

actions = tc.SFrame(data=df)

def train_model():
    global training
    training = True
    # actions = tc.SFrame.read_csv('ml-20m/ratings.csv')
    # actions = tc.SFrame.read_csv('ml-20m/ratings.csv')
    # items = tc.SFrame.read_csv('ml-20m/movies.csv')
    new_model = tc.recommender.create(actions, target="rating", user_id='userId', item_id='movieId')
    new_model.save("models/recommendations.new_model")
    training = False

train_model()

# Schedule model training every 30 minute
schedule.every(40).minutes.do(train_model)
while True:
    schedule.run_pending()
    time.sleep(1)