import datetime
from functools import total_ordering
from math import floor
from pprint import pprint
import numpy
from tensorflow import keras
import pickle

# load saved model 
pickled_model = pickle.load(open('model.pkl', 'rb'))
