import turicreate as tc
model = tc.load_model("models/recommendations.model")
items = tc.SFrame.read_csv('ml-20m/movies.csv')
results = model.recommend(users=["1"])

for result in results:
    movieId = result["movieId"]
    

for i in range(len(results)):
    print(type(results[i]))