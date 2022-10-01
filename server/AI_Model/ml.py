from tkinter import N
import tensorflow as tf
from tensorflow import keras
from keras import layers
import pandas as pd
import numpy
from data_model import DataModel

training_data = pd.read_csv('./training.csv')

features = training_data.copy()
features.pop('Delay')
features = numpy.array(features)

# normalise data
def normalize(r):
    m = DataModel()
    m.from_row(r)
    row = m.to_row_normalized()
    row.pop(5)
    return row

# normalise delay
def normalize_labels(r):
    m = DataModel()
    m.from_row([0, 0, 0, 0, 0, r])
    return m.to_row_normalized()[5]


features = numpy.array(list(map(normalize, features)))

# map delay to normalised delay
labels = training_data.pop('Delay')
labels = labels.map(normalize_labels)

# training model
model = keras.Sequential([
    layers.Dense(5),
    layers.Dense(64, activation='relu'),
    layers.Dense(2),
    layers.Dense(1)
])

# print(labels)

model.compile(loss=keras.losses.MeanSquaredError(),

              optimizer=keras.optimizers.Adam())
model.fit(features, labels, epochs=10)
# model.save("model")
# print(model.predict(features))

# test 
def predict(o):
    p = model.predict(o)
    # print(p)
    return p
