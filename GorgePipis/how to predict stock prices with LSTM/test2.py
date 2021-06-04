# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:20:10 2021

@author: Diego
"""
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def processData(data, lb):
    
    X,Y = [],[]
    
    for i in range(len(data) - lb -1):
        
        #what this is doing is getting the values and then make a new column cutting off the top value 10 times
        X.append(data[i:(i+lb), 0])
        
        #not sure what y does
        Y.append(data[(i+lb), 0])
        
    return np.array(X), np.array(Y)

data = yf.download("AMZN", start = "2019-06-01", interval = "1h", end = "2021-01-07", progress = False)[["Close"]]

#this is necesary because we want it to be a series
cl = data.Close.astype("float32")

#we want to cut the training data into 90% of what it was
train = cl[0:int(len(cl) * 0.90)]

#then we want to scale the data for scikit-learn
scl = MinMaxScaler()
scl.fit(train.values.reshape(-1,1))

#cl is what we are comparing against
new_cl = scl.transform(cl.values.reshape(-1,1))

#now we make a lookback window of 10
lb = 10
X, y = processData(new_cl, lb)

#now we want to make the training data
X_train, X_test = X[:int(X.shape[0] * 0.90)], X[int(X.shape[0] * 0.90):]
y_train, y_test = y[:int(y.shape[0] * 0.90)], y[int(X.shape[0] * 0.90):]

model = Sequential()
model.add(LSTM(256, input_shape = (lb,1)))
model.add(Dense(1))
model.compile(optimizer = "adam", loss = "mse")

X_train = X_train.reshape((X_train.shape[0],X_train.shape[1],1))
X_test = X_test.reshape((X_test.shape[0],X_test.shape[1],1))


history = model.fit(X_train,y_train,epochs=300,validation_data=(X_test,y_test),shuffle=False)


