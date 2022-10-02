from flask import request, Blueprint, jsonify, Response  
from pprint import pprint
from data_model import DataModel
import numpy
from tensorflow import keras
from math import floor
import json
from algo import wrapper
import sys
from keras.models import load_model

api = Blueprint('api', __name__)

# initialise saved model 
final_model = load_model('model.h5')

@api.route("/test", methods=['GET'])
def test():
    return jsonify({'message': 'hEllo yES woRking :")'})

# helper functions for model
def read_input(str):
    # str is request 

    # if str == 'q' or str == 'Q':
    #     return 'QUIT'

    m = DataModel()
    m.from_strdate(str)
    return m.to_row()

def predict(data):
    return final_model.predict(data)


def getRoutesAndDelay(req):
    # initialise empty array to store data
    prediction_array = []
    row_input = read_input(req['datetime'])

    # initialise empty array to store data
    prediction_array = []
    row_input.pop(5)

    # prints prediction of delay for all 32 roads
    for i in range(32):
                row_input[4] = i + 1
                mdata = DataModel()
                mdata.from_row(row_input)
                norm_row = mdata.to_row_normalized()
                norm_row.pop(5)
                prediction_array.append(norm_row)
    prediction_array = numpy.array(prediction_array)

    # predict delay
    res = predict(prediction_array)
    predicted_delays = {}

    # print(res), max delay is 30 mins
    for i in range(32):
        predicted_delays["Road " + str(i + 1)] = max(0, floor(res[i][0] * 30))

    # roads added after AI training 
    predicted_delays["Road " + str(32 + 1)] = 5
    predicted_delays["Road " + str(32 + 2)] = 10
    predicted_delays["Road " + str(32 + 3)] = 2
    predicted_delays["Road " + str(32 + 4)] = 8
    
    # algorithm to find best route here
    routes = wrapper(req['source'], req['destination'], req['datetime'], predicted_delays)
    return routes

from flask_cors import cross_origin

@api.route("/predict", methods=['POST'])
@cross_origin(supports_credentials=True)
def predictRoutes():
    req = request.get_json()

    try:
        routes = getRoutesAndDelay(req)
        print(routes)
        if routes:
            for option in routes:
                if isinstance(option['route'][0], list):
                    #js take first if its a list
                    option['route'] = option['route'][0]
                option['route'] = [int(i) for i in option['route']]
    except:
        return jsonify({'message': 'error, will come with CORS issues'})
    
    response = Response(json.dumps(routes),  mimetype='application/json')
    return response