from flask import Flask, request
from flask_restful import Resource, Api
import turicreate as tc
from flask_cors import CORS
import os 
import schedule
import shutil

app = Flask(__name__)

CORS(app)

api = Api(app)

class prediction(Resource):
    def get(self, userID, num_items_to_recommend=10):
        lastest_model = "models/recommendations.model"
        if(os.path.isdir("models/recommendations.new_model")):
            lastest_model = "models/recommendations.new_model"
        model = tc.load_model(lastest_model)
        users_list = []
        users_list.append(str(userID))
        predicts = model.recommend(users=users_list, k=num_items_to_recommend)
        res = []
        for predict in predicts:
            res.append(predict)
        if(os.path.isdir("models/recommendations.new_model")):
            shutil.rmtree("models/recommendations.model")
            os.rename("models/recommendations.new_model", "models/recommendations.model")
        return res

api.add_resource(prediction, '/recommend/<int:userID>/<int:num_items_to_recommend>')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)