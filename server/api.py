from flask import request, make_response, Blueprint, jsonify
from pprint import pprint
from data_model import DataModel
import numpy
from tensorflow import keras
from math import floor
import json
import datetime


api = Blueprint('api', __name__)

@api.route("/test", methods=['GET'])
def test():
    return jsonify({'message': 'hEllo yES woRking :")'})

@api.route('/predict', methods=['POST'])  
def predict_delay():
    def read_input():
        str = input("what is your date?")
        # if str == 'q' or str == 'Q':
        #     return 'QUIT'

        m = DataModel()
        m.from_strdate(str)
        return m.to_row()

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

    print(json.dumps(predicted_delays))
    #  return only delays of roads that trucks going through --> hvnt tested 
    total_delay = 0 
    routes = [1, 3, 4]
    for x in range(len(routes)):
        for y in range(32): 
            if x == y:
                road_delay = predicted_delays.get("Road " + str(y + 1))
                print(road_delay)
                total_delay += road_delay
    return json.dumps(predicted_delays) #returns dictionary of predicted delays at all 32 roads

# return only delays of roads that trucks going through (still need see where to implementtt)
# total_delay = 0 
# routes = [1, 3, 4] #routes that truck is going through from algo
# for x in range(len(routes)):
#     for y in range(32): 
#         if x == y:
#             road_delay = predicted_delays.get("Road " + str(y + 1))
#             print(road_delay)
#             total_delay += road_delay
# print(total_delay)
# predict_delay()