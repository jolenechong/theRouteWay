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


@api.route("/fakeoutput", methods=['POST'])
def fakeOutput():
    req = request.get_json()

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
    
    routes = wrapper(req['source'], req['destination'], req['datetime'])
    # print(routes)
    # for j in range(len(routes)):
    #     routes[j]['route'][0] = [y for z in [x.split() for x in routes[j]['route'][0]] for y in z]
    #     routes[j]['timeNeeded'] = round(routes[j]['timeNeeded'], 2)

    print(routes)
    return Response(json.dumps(routes),  mimetype='application/json')

# @api.route('/predict', methods=['POST'])  
# def predict_delay():
#     # load saved model 
#     model = keras.models.load_model('server/model')

#     def predict(data):
#         return model.predict(data, verbose=1)

#     row_input = read_input()
#     # initialise empty array to store data
#     prediction_array = []
#     row_input.pop(5)
#     # prints prediction of delay for all 32 roads
#     for i in range(32):
#                 row_input[4] = i + 1
#                 mdata = DataModel()
#                 mdata.from_row(row_input)
#                 norm_row = mdata.to_row_normalized()
#                 norm_row.pop(5)
#                 prediction_array.append(norm_row)
#     prediction_array = numpy.array(prediction_array)
#     # predict delay
#     res = predict(prediction_array)
#     predicted_delays = {}
#     # print(res), max delay is 30 mins
#     for i in range(32):
#         predicted_delays["Road " + str(i + 1)] = max(0, floor(res[i][0] * 30))
#     return predicted_delays

# return only delays of roads that trucks going through (still need see where to implementtt)
#             road_delay = predicted_delays.get("Road " + str(y + 1))
#             print(road_delay)
#             total_delay += road_delay
# print(total_delay)
# print(predict_delay())