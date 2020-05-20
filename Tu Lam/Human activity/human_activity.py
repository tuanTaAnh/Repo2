from sklearn.model_selection import train_test_split
from subprocess import check_output
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv
import os

import matplotlib.pyplot as plt
import numpy as np
import csv
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential


def Load_data(path_to_dataset):
    X = []
    Y = []

    with open(path_to_dataset + "/X_train.txt") as fx:
        data = csv.reader(fx, delimiter=" ")
        for line in data:
            for i in range(len(line)):
                try:
                    a = line[i].split(' ')
                    X.append(float(a[0]))
                except ValueError:
                    pass

    X = np.asarray(X)

    X = X.reshape(7352, 561,1)

    with open(path_to_dataset + "/Y_train.txt") as fx:
        data = csv.reader(fx, delimiter=" ")
        for line in data:
            for i in range(len(line)):
                try:
                    a = line[i].split(' ')
                    Y.append(float(a[0]))
                except ValueError:
                    pass
    return [X, Y]

def build_model():
    model = Sequential()
    layers = [1, 50, 100, 1]

    model.add(LSTM(layers[1], input_shape=(561,1), return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(layers[2], return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(layers[3]))

    model.add(Activation("linear"))

    model.compile(loss="mse", optimizer="adam",metrics=['accuracy'])

    model.summary()
    return model

def run_network():
    epochs = 1
    ratio = 0.5
    path = '/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Human activity/UCI HAR Dataset/train'

    X_train, Y_train = Load_data(path)

    model = build_model()

    print(X_train.shape)

    model.fit(X_train, Y_train, batch_size=512, nb_epoch=epochs, validation_split=0.05)

    predicted = model.predict(X_train[0])

    print(predicted)

run_network()











