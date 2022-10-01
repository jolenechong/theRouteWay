from flask import request, make_response, Blueprint, jsonify, Response  
from pprint import pprint
from data_model import DataModel
import numpy
from tensorflow import keras
from math import floor
import json
import datetime

# initialise saved model 
# model = keras.models.load_model('model')
api = Blueprint('api', __name__)

@api.route("/test", methods=['GET'])
def test():
    return jsonify({'message': 'hEllo yES woRking :")'})

import sys

@api.route("/fakeoutput", methods=['POST'])
def fakeOutput():
    # print(f"hellooooo {request.json}", file=sys.stderr)
    routes = [
        {
            "option": 1,
            "route": [[1, 3, 5]],
            "timeStart": "1.30pm",
            "timeEnd": "2.15pm",
            "destination": "A329",
            "source": "A322",
            "timeNeeded": 40,
            "delay": 0,
        },
        {
            "option": 2,
            "route": [[5, 7, 9, 11]],
            "timeStart": "5.30pm",
            "timeEnd": "6.09pm",
            "destination": "A329",
            "source": "A322",
            "timeNeeded": 39,
            "delay": 1,
            "delayTime": 9
        }
    ]
    return Response(json.dumps(routes),  mimetype='application/json')


def read_input():
    str = input("what is your date?")
    # if str == 'q' or str == 'Q':
    #     return 'QUIT'

    m = DataModel()
    m.from_strdate(str)
    return m.to_row()

@api.route('/predict', methods=['POST'])  
def predict_delay():
    # load saved model 
    model = keras.models.load_model('server/model')

    def predict(data):
        return model.predict(data, verbose=1)

    row_input = read_input()
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
    return predicted_delays

# return only delays of roads that trucks going through (still need see where to implementtt)
#             road_delay = predicted_delays.get("Road " + str(y + 1))
#             print(road_delay)
#             total_delay += road_delay
# print(total_delay)
# print(predict_delay())