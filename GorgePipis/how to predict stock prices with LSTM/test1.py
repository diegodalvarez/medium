# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:51:43 2021

@author: Diego
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

#get the data
data = yf.download("AMZN", start = '2019-06-01', interval = "1h", end = "2021-01-07", progress = False)[['Close']]

#make it into a series 
cl = data.Close.astype("float32")

#make the scaler
scl = MinMaxScaler()

#looks like it cuts the data frame into 90% of its size
train = cl[0:int(len(cl) * 0.90)]

#not sure what the fitting does but i think it changes the all the values between -1 and 1
scl.fit(train.values.reshape(-1, 1))

#not sure what this is doing
cl = scl.transform(cl.values.reshape(-1,1))

#create a function to process the data into the lookback observation and look back at the slices
def processData(data, lb):
    
    #makes two arrays
    X, Y = [],[]
    
    #iterates as many times as the size of data minus look back (10) -1
    for i in range(len(data) - lb - 1):
        
        #this puts the data into X
        X.append(data[i: (i + lb), 0])
        Y.append(data[(i + lb), 0])
        
    return np.array(X), np.array(Y)

#we make the lookback to be 10
lb = 10

#run the function
X,y = processData(cl, lb)

X_train, X_test = X[:int(X.shape[0] * 0.90)], X[int(X.shape[0] * 0.90):]
y_train, y_test = y[:int(y.shape[0] * 0.90)], y[int(y.shape[0] * 0.90):]

print("X_train.shape[0]:", X_train.shape[0], "X_train.shape[1]:", X_train.shape[1])
print("X_test.shape[0]:", X_test.shape[0], "X_test.shape[1]:", X_test.shape[1])
print("y_train.shape[0]:", y_train.shape[0])
print("y_trian.shape[0]:", y_test.shape[0])


#making the model
model = Sequential()
model.add(LSTM(256, input_shape = (lb,1)))
model.add(Dense(1))
model.compile(optimizer = "adam", loss = "mse")


#reshape the data
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

#fitting the model and checking for overfitting
history = model.fit(X_train, y_train, epochs = 300, validaiton_data = (X_test, y_test), shuffle = False)



