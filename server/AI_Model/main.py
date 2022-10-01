import datetime
from functools import total_ordering
from math import floor
from pprint import pprint
from data_model import DataModel
import numpy
from tensorflow import keras


def read_input():
    str = input()
    # if str == 'q' or str == 'Q':
    #     return 'QUIT'

    m = DataModel()
    m.from_strdate(str)
    return m.to_row()

# load saved model 
model = keras.models.load_model('model')


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
# print(res), max delay is 30 mins
for i in range(32):
    print("Road " + str(i + 1) + ": " + str(max(0, floor(res[i][0] * 30))) + " minutes")



# while 1:
#     try:
#         row_input = read_input()
#         if row_input == 'QUIT':
#             break

#         prediction_array = []

#         row_input.pop(5)
#         for i in range(32):
#             row_input[4] = i + 1
#             mdata = DataModel()
#             mdata.from_row(row_input)
#             norm_row = mdata.to_row_normalized()
#             norm_row.pop(5)
#             prediction_array.append(norm_row)

#         # print(prediction_array)
#         prediction_array = numpy.array(prediction_array)
#         # print(prediction_array)

#         res = predict(prediction_array)
#         # min = round(res * 30)
#         for i in range(32):
#             print("Road " + str(i + 1) + ": " +
#                   str(max(0, floor(res[i][0] * 30))) + " minutes")
#     except:
#         print("Try again: enter a year between 2016-2024 & make sure the format is 0")
