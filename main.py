import turicreate as tc
import os 
import schedule
import time

training = False  # Initialize the training flag

def train_model():
    global training
    training = True
    # actions = tc.SFrame.read_csv('ml-20m/ratings.csv')
    actions = tc.SFrame.read_csv('ml-20m/ratings.csv')
    items = tc.SFrame.read_csv('ml-20m/movies.csv')
    new_model = tc.recommender.create(actions, target="rating", user_id='userId', item_id='movieId', item_data=items)
    new_model.save("models/recommendations.new_model")
    training = False

train_model()

# Schedule model training every 30 minute
schedule.every(30).minutes.do(train_model)
while True:
    schedule.run_pending()
    time.sleep(1)